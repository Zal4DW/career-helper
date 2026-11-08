# CV PDF Scripts

This file holds the two Python scripts that `cv-pdf-production.md` uses: `generate_cv_pdf.py` renders a markdown CV or cover letter to an ATS-safe PDF, and `verify_cv_pdf.py` checks the PDF before it is shared. They are kept inside Markdown so the plugin ships only text files.

**How to use them:** when a verified PDF is needed, copy each script below, exactly as written and without the fence lines, into a file with the name given in its heading, in a `.career-helper-tools/` folder inside the application folder that holds `cv-optimised.md`. Then run them as `cv-pdf-production.md` describes. They need Python 3 with the `markdown`, `weasyprint`, and `pypdf` packages; the page images also need the `pdf2image` package and the Poppler system tools (`cv-pdf-production.md` gives the install commands). Write them fresh each session rather than editing them.

## generate_cv_pdf.py

~~~~python
"""Render a markdown CV (or cover letter) to an ATS-safe PDF.

Adapted from the ODTA document-generator reference implementation and the
career-helper guide builder. Produces a deliberately plain, single-column
document: real text (never images of text), standard fonts, standard
headings, and no layout tricks that confuse applicant tracking systems.

Dependencies (not part of the plugin runtime):
    pip install markdown weasyprint

Usage:
    python3 generate_cv_pdf.py cv-optimised.md cv.pdf
    python3 generate_cv_pdf.py cv-optimised.md cv.pdf --theme compact
    python3 generate_cv_pdf.py cv-optimised.md cv.html --html-only

If WeasyPrint is unavailable, use --html-only and print the HTML to PDF
from a browser (or via headless Chromium). The HTML uses the same CSS, so
the result is equivalent.

After generating, ALWAYS verify with verify_cv_pdf.py before the CV is
sent anywhere. See references/cv-pdf-production.md for the full loop.
"""
import argparse
import re
import sys
from pathlib import Path

# ATS-safe styling. Deliberately boring:
# - single column, no floats, no text in headers/footers except page number
# - system fonts with wide fallbacks
# - generous margins so nothing is clipped by scanners or print
# - headings kept with their following content to avoid orphaned titles
BASE_CSS = """
@page {
  size: A4;
  margin: %(page_margin)s;
  @bottom-right {
    content: counter(page) " of " counter(pages);
    font-family: Arial, Helvetica, sans-serif;
    font-size: 8pt;
    color: #666666;
  }
}
html { font-size: %(base_font)s; }
body {
  font-family: Arial, Helvetica, 'Segoe UI', sans-serif;
  color: #1f1f1f;
  line-height: %(line_height)s;
  margin: 0;
}
h1 {
  font-size: 1.9em;
  margin: 0 0 2pt 0;
  line-height: 1.15;
  color: #111111;
}
/* The line straight after the name: contact details or headline. */
h1 + p { margin-top: 0; color: #333333; }
h2 {
  font-size: 1.15em;
  text-transform: uppercase;
  letter-spacing: 0.03em;
  color: #111111;
  border-bottom: 1pt solid #999999;
  padding-bottom: 2pt;
  margin: 14pt 0 6pt 0;
  page-break-after: avoid;
}
h3 {
  font-size: 1.0em;
  margin: 10pt 0 2pt 0;
  page-break-after: avoid;
}
/* Keep a role heading with at least the start of its bullets. */
h3 + p, h3 + ul { page-break-before: avoid; }
p { margin: 0 0 5pt 0; }
ul, ol { margin: 0 0 6pt 0; padding-left: 16pt; }
li { margin: 0 0 2.5pt 0; }
li > p { margin: 0; }
strong { color: #111111; }
a { color: #1f1f1f; text-decoration: none; }
hr { border: none; border-top: 0.5pt solid #bbbbbb; margin: 10pt 0; }
/* Tables parse badly in many ATS pipelines; if the markdown insists on
   one, keep it simple and visible rather than hiding the problem. */
table { border-collapse: collapse; width: 100%%; margin: 0 0 8pt 0; }
th, td {
  border: 0.5pt solid #999999;
  padding: 3pt 6pt;
  text-align: left;
  font-size: 0.92em;
}
blockquote {
  margin: 0 0 6pt 0;
  padding-left: 8pt;
  border-left: 2pt solid #999999;
  color: #333333;
}
"""

THEMES = {
    # Comfortable reading; the default for most CVs.
    "standard": {"page_margin": "18mm 16mm 18mm 16mm", "base_font": "10.5pt", "line_height": "1.4"},
    # Tighter; for experienced candidates fighting the two-page limit.
    "compact": {"page_margin": "14mm 14mm 16mm 14mm", "base_font": "10pt", "line_height": "1.3"},
    # Larger print; also suits cover letters.
    "relaxed": {"page_margin": "22mm 20mm 22mm 20mm", "base_font": "11pt", "line_height": "1.5"},
}

HTML_SHELL = """<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>{css}</style>
</head>
<body>
{body}
</body>
</html>
"""


def build_html(src: Path, theme: str) -> str:
    """Convert the markdown source to a styled HTML document string.

    Fails closed if unresolved {{PLACEHOLDER}} markers remain, so a
    template can never be rendered into a submission document.
    """
    try:
        import markdown
    except ImportError:
        sys.exit("Missing dependency: pip install markdown")

    text = src.read_text(encoding="utf-8")
    placeholders = sorted(set(re.findall(r"\{\{[^{}]*\}\}", text)))
    if placeholders:
        shown = ", ".join(placeholders[:10]) + (" ..." if len(placeholders) > 10 else "")
        sys.exit(
            f"Refusing to generate: {len(placeholders)} unresolved placeholder(s) "
            f"in {src}: {shown}\n"
            "Fill them in first; a submission document must never carry template markers."
        )
    body = markdown.markdown(
        text,
        extensions=["tables", "sane_lists", "attr_list"],
        output_format="html5",
    )
    css = BASE_CSS % THEMES[theme]
    # Title from the first heading, for the PDF metadata ATS systems read.
    title = next(
        (line.lstrip("# ").strip() for line in text.splitlines() if line.startswith("# ")),
        src.stem,
    )
    return HTML_SHELL.format(title=title, css=css, body=body)


def main() -> None:
    """Parse arguments, render the document, and report the next step."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("source", type=Path, help="Markdown CV or cover letter")
    parser.add_argument("output", type=Path, help="Output .pdf (or .html with --html-only)")
    parser.add_argument("--theme", choices=sorted(THEMES), default="standard")
    parser.add_argument(
        "--html-only",
        action="store_true",
        help="Write styled HTML instead of PDF (fallback when WeasyPrint is unavailable)",
    )
    args = parser.parse_args()

    if not args.source.exists():
        sys.exit(f"Source not found: {args.source}")

    html = build_html(args.source, args.theme)

    if args.html_only:
        args.output.write_text(html, encoding="utf-8")
        print(f"Wrote {args.output} (print to PDF from a browser, A4, default margins off)")
        return

    try:
        from weasyprint import HTML
    except ImportError:
        sys.exit(
            "Missing dependency: pip install weasyprint\n"
            "Or re-run with --html-only and print the HTML to PDF from a browser."
        )
    HTML(string=html).write_pdf(str(args.output))
    print(f"Wrote {args.output} (theme: {args.theme})")
    print("Now verify it: python3 verify_cv_pdf.py", args.output, args.source)


if __name__ == "__main__":
    main()
~~~~

## verify_cv_pdf.py

~~~~python
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


def _drop_heading_marker(line: str) -> str:
    """Remove a leading markdown heading marker (up to three spaces of
    indent, one to six hashes, then whitespace) from a single line."""
    body = line.lstrip(" \t")
    if len(line) - len(body) > 3:
        return line
    hashes = len(body) - len(body.lstrip("#"))
    if 1 <= hashes <= 6 and body[hashes:hashes + 1].isspace():
        return " " + body[hashes + 1:]
    return line


def strip_markdown(text: str) -> str:
    """Reduce markdown to roughly the text a reader (or ATS parser) sees.

    Removes fenced code blocks, link targets, heading markers, and
    emphasis or code punctuation, so syntax is never counted as content.
    """
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"\]\([^)]*\)", "] ", text)
    text = "\n".join(_drop_heading_marker(line) for line in text.split("\n"))
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
~~~~
