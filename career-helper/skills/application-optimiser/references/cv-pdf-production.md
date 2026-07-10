# CV PDF Production

**Purpose:** Turn a finished markdown CV or cover letter into a submission-ready PDF, then prove it survived the journey: the layout renders cleanly and the text layer parses the way an applicant tracking system will actually read it. A CV that looks right but parses wrong fails silently; this pipeline exists to catch that before an employer does.

**Scripts:** `scripts/generate_cv_pdf.py` and `scripts/verify_cv_pdf.py` (relative to this skill's folder)

---

## When to Offer

- The optimised CV (`cv-optimised.md`) or cover letter is finished and the user is ready to submit.
- The user asks for "a PDF of my CV", "something I can upload", or a recruiter has asked for a PDF.

Do not offer PDF production for drafts still in review; the markdown remains the working format, and the PDF is regenerated from it. If content changes, change the markdown and regenerate; never edit a PDF.

Ask one question before generating: does the employer want PDF or Word? Some ATS configurations and agencies still prefer `.docx`. If the answer is Word, produce the best markdown and advise converting via a word processor; this pipeline covers PDF.

---

## Why the Output Is Deliberately Plain

ATS parsers reward boring documents. The built-in styling is single column with standard fonts (Arial with wide fallbacks), standard section headings, real text throughout, and page numbers as the only page furniture. It avoids the classic parse-killers:

- Multi-column layouts (parsers read across columns, scrambling the order)
- Text in headers and footers (often ignored by parsers; contact details die there)
- Tables for layout, text boxes, and graphics
- Text rendered as images (invisible to parsers entirely)
- Fonts below 10pt as a way of cheating the page limit

If the user wants a visually designed CV for humans (portfolio roles, design roles), produce that as a second artefact and keep the plain version for ATS uploads. Never pretend one file serves both purposes well.

---

## The Generate-Verify Loop

Dependencies (one-time, not part of the plugin runtime): `pip install markdown weasyprint pypdf pdf2image`, plus the poppler system package for page images (`apt-get install poppler-utils` or `brew install poppler`).

Run from the application folder so outputs land beside the CV.

**1. Generate.**

```bash
python3 {skill}/scripts/generate_cv_pdf.py cv-optimised.md cv.pdf --theme standard
```

Themes: `standard` (default), `compact` (experienced candidates fighting the two-page limit), `relaxed` (larger print; suits cover letters). The script warns if unfilled `{{PLACEHOLDER}}` markers remain; never generate a submission PDF from a template with placeholders.

**2. Verify.**

```bash
python3 {skill}/scripts/verify_cv_pdf.py cv.pdf cv-optimised.md
```

The verifier checks the text layer (pages with too few extractable words; content words present in the markdown but missing from the PDF) and flags documents over the page limit (default two pages; pass `--max-pages 0` to skip, for example for an academic CV). It also renders each page to `pdf-check/page_N.png`.

**3. Inspect the page images.** Read each PNG with the Read tool and check like a human reviewer:

- Orphaned headings: a section or role title stranded at the bottom of a page with its content overleaf
- Overflow: text touching margins, truncated lines, or a surprise third page
- Spacing: cramped bullets, uneven gaps between sections
- The name and contact line: present, at the top, on page one

**4. Fix and repeat.** Fix problems in the markdown (cut content, reorder sections) or switch theme, regenerate, and re-verify. Do not ship on a failed check, and do not weaken the check to pass it. The loop typically converges in one or two passes.

**5. Report.** Tell the user what was verified, in one short block: page count, text-layer result (PASS or what failed), and anything the visual inspection caught and fixed. Delete or ignore the `pdf-check/` images afterwards; they are working files.

---

## Fallbacks

**WeasyPrint unavailable and cannot be installed:** generate styled HTML instead and have the user print it to PDF from their browser (A4, default margins off, headers and footers disabled):

```bash
python3 {skill}/scripts/generate_cv_pdf.py cv-optimised.md cv.html --html-only
```

Then run the verifier on whatever PDF the browser produced; the checks still apply.

**Claude environments with native document rendering** (for example Claude Cowork) can produce a PDF directly from the markdown. That is acceptable for a quick draft, but the verification step is not optional either way: whatever produced the PDF, run `verify_cv_pdf.py` on the result before it is submitted. The value of this pipeline is the verified loop, not the particular renderer.

**pdf2image or poppler missing:** the verifier skips the visual render and says so. The text-layer check still runs. Find another way to eyeball the pages (open the PDF, or Read it directly) before the file goes anywhere.

---

## Output

**Files:** `applications/{role-slug}/cv.pdf` (and `cover-letter.pdf` when requested), regenerated from the markdown sources in the same folder.

**Content integrity:** the PDF contains exactly what the markdown contains. This pipeline changes formatting, never words. Content fixes go through the CV optimisation capability first.
