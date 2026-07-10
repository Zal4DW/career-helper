#!/usr/bin/env python3
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
