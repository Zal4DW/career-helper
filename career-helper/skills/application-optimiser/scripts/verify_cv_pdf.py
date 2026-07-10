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

# Words that appear in markdown syntax or boilerplate, not content.
STOPWORDS = {
    "the", "and", "for", "with", "from", "into", "that", "this", "are",
    "was", "were", "have", "has", "had", "will", "would", "can", "could",
    "not", "but", "all", "its", "their", "them", "they", "you", "your",
    "per", "via", "our", "out", "over", "under", "between", "across",
}


def extract_text_per_page(pdf_path: Path):
    try:
        from pypdf import PdfReader
    except ImportError:
        sys.exit("Missing dependency: pip install pypdf")
    reader = PdfReader(str(pdf_path))
    return [(page.extract_text() or "") for page in reader.pages]


def content_words(text: str):
    words = re.findall(r"[A-Za-z][A-Za-z+#.'-]{2,}", text.lower())
    return {w for w in words if w not in STOPWORDS}


def check_text_layer(pages, source) -> list:
    problems = []
    for i, text in enumerate(pages, start=1):
        word_count = len(text.split())
        if word_count < 20:
            problems.append(
                f"Page {i} has only {word_count} extractable words. "
                "An ATS will see an almost-empty page."
            )
    if source and source.exists():
        src_words = content_words(source.read_text(encoding="utf-8"))
        # Substring match rather than token match: extraction can merge
        # adjacent blocks ("NameLondon"), which is not a lost word.
        pdf_text = "\n".join(pages).lower()
        missing = sorted(w for w in src_words if w not in pdf_text)
        if missing:
            shown = ", ".join(missing[:15]) + (" ..." if len(missing) > 15 else "")
            problems.append(
                f"{len(missing)} content words from the source are missing from "
                f"the PDF text layer: {shown}"
            )
    return problems


def render_pages(pdf_path: Path, pages_dir: Path) -> list:
    """Render each page to PNG for visual inspection. Returns image paths."""
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
    images = convert_from_path(str(pdf_path), dpi=150)
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
