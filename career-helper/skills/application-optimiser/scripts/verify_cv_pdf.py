#!/usr/bin/env python3
"""Verify a generated CV PDF before it goes anywhere near an employer.

Two checks, mirroring what happens to the document after submission:

1. ATS text-layer check: extract the text layer the way parsing software
   does, and confirm the content survived. Reports pages with little or no
   extractable text (a scanned or image-based CV fails ATS parsing
   entirely) and content words from the markdown source that never made it
   into the text layer.

2. Visual check: render each page to a PNG so Claude (or the user) can
   inspect the real layout: orphaned headings at page bottoms, overflow,
   cramped margins, or a CV that silently grew to three pages.

Adapted from the ODTA pdf-toolkit verification scripts.

Dependencies (not part of the plugin runtime):
    pip install pypdf pdf2image     # pdf2image also needs the poppler
                                    # system package (pdftoppm)

Usage:
    python3 verify_cv_pdf.py cv.pdf [source.md] [--pages-dir DIR] [--max-pages 2]

Exit code is non-zero when a check fails, so the generate-verify loop can
stop and fix rather than ship.
"""
import argparse
import re
import sys
from pathlib import Path

# Common words excluded from the missing-content comparison. Two-letter
# technical terms the CV cares about (AI, ML, BI, QA) are NOT stopwords.
STOPWORDS = {
    "the", "and", "for", "with", "from", "into", "that", "this", "are",
    "was", "were", "have", "has", "had", "will", "would", "can", "could",
    "not", "but", "all", "its", "their", "them", "they", "you", "your",
    "per", "via", "our", "out", "over", "under", "between", "across",
    "of", "to", "in", "at", "on", "by", "an", "as", "is", "it", "or",
    "we", "be", "do", "if", "my", "no", "so", "up", "us", "am", "he",
    "she", "his", "her",
}

WORD_RE = re.compile(r"[A-Za-z][A-Za-z+#.'-]+")


def extract_text_per_page(pdf_path: Path):
    """Return the extractable text of each page, in page order."""
    try:
        from pypdf import PdfReader
    except ImportError:
        sys.exit("Missing dependency: pip install pypdf")
    reader = PdfReader(str(pdf_path))
    return [(page.extract_text() or "") for page in reader.pages]


def strip_markdown(text: str) -> str:
    """Reduce markdown to roughly the text a reader (or ATS parser) sees.

    Removes fenced code blocks, link targets, heading markers, and
    emphasis or code punctuation, so syntax is never counted as content.
    """
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"\]\([^)]*\)", "] ", text)
    text = re.sub(r"^\s{0,3}#{1,6}\s", " ", text, flags=re.M)
    return text.replace("`", " ").replace("*", " ").replace("_", " ")


def content_words(text: str):
    """Tokenise into lowercase content words (2+ letters, stopwords out)."""
    return {w for w in (m.group(0).lower() for m in WORD_RE.finditer(text))
            if w not in STOPWORDS}


def pdf_tokens(pages) -> set:
    """Tokenise extracted PDF text, splitting block-merge artefacts.

    Extraction can join adjacent blocks without whitespace
    ("NameLondon"); inserting a break at lower-to-upper transitions
    recovers the real words without letting "java" match "javascript".
    """
    text = "\n".join(pages)
    text = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", text)
    return content_words(text)


def check_text_layer(pages, source) -> list:
    """Return a list of text-layer problems (empty means the check passed)."""
    problems = []
    for i, text in enumerate(pages, start=1):
        word_count = len(text.split())
        if word_count < 20:
            problems.append(
                f"Page {i} has only {word_count} extractable words. "
                "An ATS will see an almost-empty page."
            )
    if source and source.exists():
        src_words = content_words(strip_markdown(source.read_text(encoding="utf-8")))
        missing = sorted(src_words - pdf_tokens(pages))
        if missing:
            shown = ", ".join(missing[:15]) + (" ..." if len(missing) > 15 else "")
            problems.append(
                f"{len(missing)} content words from the source are missing from "
                f"the PDF text layer: {shown}"
            )
    return problems


def render_pages(pdf_path: Path, pages_dir: Path) -> list:
    """Render each page to PNG for visual inspection. Returns image paths.

    Skips (with a note) rather than aborting when pdf2image or the
    poppler system package is unavailable; the text-layer check is
    independent of the visual one.
    """
    try:
        from pdf2image import convert_from_path
    except ImportError:
        print(
            "NOTE: pdf2image not installed (pip install pdf2image, plus the "
            "poppler system package); skipping the visual render. Inspect "
            "the PDF another way before sending it.",
            file=sys.stderr,
        )
        return []
    pages_dir.mkdir(parents=True, exist_ok=True)
    try:
        images = convert_from_path(str(pdf_path), dpi=150)
    except Exception as exc:  # poppler missing or broken at runtime
        print(
            f"NOTE: page rendering failed ({exc.__class__.__name__}: {exc}); "
            "skipping the visual render. Install the poppler system package "
            "and inspect the PDF before sending it.",
            file=sys.stderr,
        )
        return []
    paths = []
    for i, image in enumerate(images, start=1):
        # Keep inspection images a sensible size.
        if image.width > 1200:
            ratio = 1200 / image.width
            image = image.resize((1200, int(image.height * ratio)))
        out = pages_dir / f"page_{i}.png"
        image.save(out)
        paths.append(out)
    return paths


def main() -> None:
    """Run both checks, print the report, and exit non-zero on failure."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("pdf", type=Path)
    parser.add_argument("source", type=Path, nargs="?", help="Markdown source to compare against")
    parser.add_argument("--pages-dir", type=Path, default=None,
                        help="Directory for page PNGs (default: <pdf-dir>/pdf-check)")
    parser.add_argument("--max-pages", type=int, default=2,
                        help="Flag the document if it exceeds this many pages (default 2; use 0 to skip)")
    args = parser.parse_args()

    if not args.pdf.exists():
        sys.exit(f"PDF not found: {args.pdf}")

    pages = extract_text_per_page(args.pdf)
    problems = check_text_layer(pages, args.source)

    if args.max_pages and len(pages) > args.max_pages:
        problems.append(
            f"Document is {len(pages)} pages (limit set to {args.max_pages}). "
            "Cut content or use the compact theme; do not shrink the font below 10pt."
        )

    pages_dir = args.pages_dir or (args.pdf.parent / "pdf-check")
    images = render_pages(args.pdf, pages_dir)

    print(f"Pages: {len(pages)}")
    for i, text in enumerate(pages, start=1):
        print(f"  page {i}: {len(text.split())} extractable words")
    if images:
        print("Page images for visual inspection:")
        for p in images:
            print(f"  {p}")
        print("Inspect each image for orphaned headings, overflow, and cramped spacing.")

    if problems:
        print("\nFAIL:")
        for p in problems:
            print(f"  - {p}")
        sys.exit(1)
    print("\nPASS: text layer looks parseable. Visual inspection still required.")


if __name__ == "__main__":
    main()
