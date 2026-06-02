#!/usr/bin/env python3
"""Render the getting-the-best guide markdown to a styled PDF.

Regenerate the shareable guide whenever its markdown source changes, so the
PDF does not drift out of date.

Dependencies (not part of the plugin runtime):
    pip install markdown weasyprint

Usage:
    python3 scripts/build-guide-pdf.py \\
        career-helper/skills/getting-started/references/getting-the-best-guide.md \\
        career-helper/skills/getting-started/references/getting-the-best-guide.pdf
"""
import sys
import markdown
from weasyprint import HTML

SRC, OUT = sys.argv[1], sys.argv[2]

with open(SRC, encoding="utf-8") as fh:
    text = fh.read()

html_body = markdown.markdown(
    text,
    extensions=["tables", "fenced_code", "sane_lists", "attr_list", "toc"],
    output_format="html5",
)

CSS = """
@page {
  size: A4;
  margin: 22mm 18mm 20mm 18mm;
  @bottom-center {
    content: "Career Helper  |  Prosper AI Consulting, UK";
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 8pt;
    color: #8a8f98;
  }
  @bottom-right {
    content: counter(page);
    font-family: 'Helvetica Neue', Arial, sans-serif;
    font-size: 8pt;
    color: #8a8f98;
  }
}
html { font-size: 10.5pt; }
body {
  font-family: 'Helvetica Neue', 'Segoe UI', Arial, sans-serif;
  color: #25282d;
  line-height: 1.5;
}
h1 {
  font-size: 23pt;
  color: #1a4d8f;
  border-bottom: 2px solid #1a4d8f;
  padding-bottom: 6px;
  margin: 0 0 14px 0;
  line-height: 1.2;
}
h2 {
  font-size: 15pt;
  color: #1a4d8f;
  margin: 22px 0 8px 0;
  padding-top: 4px;
  border-top: 1px solid #e2e6ec;
  page-break-after: avoid;
}
h3 {
  font-size: 12pt;
  color: #2f3640;
  margin: 16px 0 6px 0;
  page-break-after: avoid;
}
p { margin: 0 0 8px 0; }
ul, ol { margin: 0 0 10px 0; padding-left: 20px; }
li { margin: 0 0 3px 0; }
strong { color: #1f2329; }
a { color: #1a4d8f; text-decoration: none; }
code {
  font-family: 'SF Mono', 'Consolas', 'Liberation Mono', monospace;
  font-size: 9pt;
  background: #f2f4f7;
  padding: 1px 4px;
  border-radius: 3px;
}
pre {
  background: #f6f8fa;
  border: 1px solid #e2e6ec;
  border-radius: 5px;
  padding: 10px 12px;
  font-size: 8.5pt;
  line-height: 1.35;
  white-space: pre-wrap;
  word-wrap: break-word;
  page-break-inside: avoid;
}
pre code { background: none; padding: 0; font-size: 8.5pt; }
table {
  border-collapse: collapse;
  width: 100%;
  margin: 8px 0 14px 0;
  font-size: 9.5pt;
  page-break-inside: avoid;
}
th, td {
  border: 1px solid #d7dce3;
  padding: 5px 8px;
  text-align: left;
  vertical-align: top;
}
th { background: #eef2f7; color: #1a4d8f; }
tr:nth-child(even) td { background: #fafbfc; }
hr { border: none; border-top: 1px solid #e2e6ec; margin: 16px 0; }
blockquote {
  margin: 8px 0;
  padding: 4px 14px;
  border-left: 3px solid #1a4d8f;
  color: #3a4049;
  background: #f7f9fb;
}
em { color: #3a4049; }
"""

full = f"""<!DOCTYPE html>
<html lang="en-GB"><head><meta charset="utf-8">
<title>Getting the Best from Career Helper</title>
<style>{CSS}</style></head><body>{html_body}</body></html>"""

HTML(string=full, base_url=".").write_pdf(OUT)
print("wrote", OUT)
