# PCCOE AIML Assignment Design & Layout Specification

This document serves as the absolute source of truth for generating, styling, and formatting assignments for the **Artificial Intelligence and Machine Learning (AIML)** course at PCCOE. Any AI assisting with creating or editing assignments must strictly adhere to these rules to ensure the exact visual presentation, high academic rigor, and clean physical print layout established in DAA Assignment 6.

---

## 1. Core Architecture
- **HTML Structure**: Assignments are built as single, self-contained HTML files.
- **Visual Page Cuts**: The document is NOT a single continuous white block. It must be broken down into individual `<div class="page">` blocks to simulate physical sheets of paper on screen.
- **Editable Mode**: The main container must have `contenteditable="true"` so the user can edit text or paste screenshots directly in their browser before printing.
- **No Footers**: There are strictly NO footers (`.page-footer`, `.print-footer`, page number strips, etc.). Do not generate them.

---

## 2. Page Dimensions & Dual-Padding System
This is the most critical formatting mechanism. The assignment must look like a beautifully padded, readable document on screen, while printing with exact zero-margin margins to eliminate browser artifacts and save paper.

### Screen CSS (The "Preview")
```css
body {
  font-family: Arial, sans-serif;
  font-size: 11pt;
  line-height: 1.6;
  color: #000;
  background: #e5e7eb; /* Neutral grey canvas outside physical pages */
  padding: 20px;
}

.container {
  max-width: 8.5in;
  margin: 0 auto;
}

.page {
  min-height: 11in;
  width: 8.5in;
  padding: 0.7in 0.8in; /* Generous margins for screen preview */
  background: #ffffff;
  margin: 0 auto 24px auto;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  position: relative;
  box-sizing: border-box;
}

.page:focus-within {
  outline: 2px dashed #4299e1; /* Visual cue when editing */
}
```

### Print CSS (`@media print` & `@page`)
To completely suppress browser-generated default headers (page URL, webpage title) and footers (date, auto-generated page numbers), the CSS `@page` rule must set `margin: 0`. The actual physical margins on paper are cleanly provided via internal padding on `.page`:

```css
/* Print CSS: Clean A4 formatting with zero browser header/footer */
@page {
  size: A4 portrait;
  margin: 0; /* Completely suppresses browser header (title/URL) and footer (date/page #) */
}

@media print {
  * {
    outline: none !important;
    box-shadow: none !important;
  }
  html, body {
    background: #ffffff !important;
    padding: 0 !important;
    margin: 0 !important;
    width: 100% !important;
    -webkit-print-color-adjust: exact !important;
    print-color-adjust: exact !important;
  }
  .container {
    max-width: 100% !important;
    width: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
    box-shadow: none !important;
    border: none !important;
  }
  .page {
    width: 100% !important;
    min-height: 297mm !important;
    box-sizing: border-box !important;
    margin: 0 !important;
    padding: 12mm 15mm !important; /* Internal page margin so text doesn't touch paper edges */
    box-shadow: none !important;
    border: none !important;
    outline: none !important;
    page-break-after: always !important;
    break-after: page !important;
    page-break-inside: avoid !important;
    break-inside: avoid !important;
  }
  .page:last-child {
    page-break-after: avoid !important;
    break-after: avoid !important;
  }
  .page:focus, .page:focus-within {
    outline: none !important;
    border: none !important;
    box-shadow: none !important;
  }
  pre, code {
    white-space: pre-wrap !important;
    word-break: break-all !important;
  }
  h2, h3 {
    page-break-after: avoid !important;
    break-after: avoid !important;
  }
  .styled-table, .cover-table, .diagram-container, 
  .code-window-light, .terminal-window, .math-callout, .algo-container, .info-box {
    page-break-inside: avoid !important;
    break-inside: avoid !important;
  }
  li {
    page-break-inside: avoid !important;
    break-inside: avoid !important;
  }
}
```

---

## 3. Cover Page Table
Every AIML assignment must begin with this exact structured metadata table inside the first `.page`.
- Font: `Times New Roman`
- Borders: `1px solid #000`
- Logo width: 18% of table

**HTML Template:**
```html
<table class="cover-table">
  <tr>
    <td class="logo-container">
      <img src="pccoelogo.jfif" alt="PCCOE Logo" contenteditable="false">
    </td>
    <td class="college-info">
      Pimpri Chinchwad Education Trust's<br>
      Pimpri Chinchwad College of Engineering
    </td>
  </tr>
  <tr>
    <td colspan="2" class="row-centered">
      Assignment No. [X]
    </td>
  </tr>
  <tr>
    <td colspan="2" class="row-left">
      Course:- Artificial Intelligence and Machine Learning
    </td>
  </tr>
  <tr>
    <td colspan="2" class="row-left">
      Name:- Aditya Chandrajit Deore
    </td>
  </tr>
  <tr>
    <td colspan="2" class="row-left">
      PRN:- 124B1F116
    </td>
  </tr>
  <tr>
    <td colspan="2" class="row-left">
      Batch:- B3
    </td>
  </tr>
</table>
```

**Cover Table CSS:**
```css
.cover-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 24px;
  font-family: 'Times New Roman', Times, serif;
}
.cover-table td {
  border: 1px solid #000;
  padding: 7px 12px;
}
.cover-table .college-info {
  text-align: center;
  font-weight: bold;
  font-size: 15pt;
  line-height: 1.35;
}
.cover-table .row-centered { text-align: center; font-weight: bold; font-size: 13pt; }
.cover-table .row-left { text-align: left; font-weight: bold; font-size: 12pt; }
.logo-container { text-align: center; width: 18%; padding: 4px !important; }
.logo-container img { max-width: 90px; height: auto; display: block; margin: 0 auto; }
```

---

## 4. Typography, Tables & Visual Components

### Headings and Text
- **Section Headings (`h2`)**: `Arial, sans-serif`, `14pt`, `font-weight: bold`, `color: #000`, `margin-top: 24px`, `margin-bottom: 12px`, `border-bottom: 1.5px solid #cbd5e1`, `padding-bottom: 5px`.
  - First `h2` on a page must have `margin-top: 0;`.
- **Subheadings (`h3`)**: `Arial, sans-serif`, `12pt`, `font-weight: bold`, `color: #000`, `margin-top: 18px`, `margin-bottom: 8px`.
- **Paragraphs (`p`)**: `Arial, sans-serif`, `10.5pt`, `text-align: justify`, `line-height: 1.6`, `margin-bottom: 12px`.
- **Lists (`ul`, `ol`)**: `margin-left: 24px`, `font-size: 10.5pt`, `line-height: 1.6`, `margin-bottom: 14px`.

### Data Tables (`.styled-table`)
```css
table.styled-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
  margin-bottom: 20px;
  font-size: 9.5pt;
  font-family: Arial, sans-serif;
}
table.styled-table th, table.styled-table td {
  border: 1px solid #000;
  padding: 7px 10px;
  text-align: left;
}
table.styled-table th {
  background-color: #f2f2f2;
  font-weight: bold;
  text-align: center;
}
table.styled-table td.center { text-align: center; }
```

### Mathematical Callout Box (`.math-callout`)
```css
.math-callout {
  background: #f8fafc;
  border: 1px solid #cbd5e1;
  border-radius: 6px;
  padding: 12px 18px;
  margin: 12px 0 20px 0;
  text-align: center;
  font-size: 10pt;
}
```

### Modern Code Window (`.code-window-light`)
Assignments use an elegant macOS-inspired code window with traffic light window controls:
```css
.code-window-light {
  background-color: #ffffff;
  border-radius: 6px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  margin: 12px 0 20px 0;
  overflow: hidden;
  border: 1px solid #d1d5db;
}
.code-header-light {
  background-color: #f3f4f6;
  padding: 6px 14px;
  display: flex;
  align-items: center;
  border-bottom: 1px solid #e5e7eb;
}
.code-dots {
  display: flex;
  gap: 5px;
  margin-right: 10px;
}
.code-dot {
  width: 9px;
  height: 9px;
  border-radius: 50%;
  display: inline-block;
}
.dot-red { background-color: #ff5f56; }
.dot-yellow { background-color: #ffbd2e; }
.dot-green { background-color: #27c93f; }
.code-title-light {
  color: #374151;
  font-size: 9pt;
  font-family: 'Segoe UI', sans-serif;
  font-weight: 600;
}
pre[class*="language-"] {
  border: none !important;
  border-radius: 0 !important;
  font-size: 8.5pt !important;
  line-height: 1.38;
  padding: 12px 16px !important;
  margin: 0 !important;
  background: #fafafa !important;
}
code[class*="language-"] {
  font-family: Consolas, Monaco, monospace !important;
  font-size: 8.5pt !important;
}
```

### Authentic Terminal Console Window (`.terminal-window`)
Python execution output must be presented in a realistic, dark engineering terminal without neon or fluorescent distractors:
```css
.terminal-window {
  background-color: #1e222a;
  border-radius: 6px;
  box-shadow: 0 3px 12px rgba(0, 0, 0, 0.2);
  margin: 12px 0 20px 0;
  overflow: hidden;
  border: 1px solid #333;
}
.terminal-header {
  background-color: #282c34;
  padding: 6px 14px;
  display: flex;
  align-items: center;
  border-bottom: 1px solid #3e4451;
}
.terminal-title {
  color: #9da5b4;
  font-size: 8.5pt;
  font-family: 'Segoe UI', sans-serif;
}
.terminal-body {
  padding: 14px 16px;
  font-family: Consolas, 'Courier New', monospace;
  font-size: 8.5pt;
  line-height: 1.42;
  color: #abb2bf;
  white-space: pre;
}
.prompt-text { color: #98c379; }
.cmd-text { color: #61afef; font-weight: bold; }
```

---

## 5. External Libraries
Always include MathJax, Prism.js, and Mermaid in the `<head>`:
```html
<!-- MathJax for formulas -->
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

<!-- Prism.js for code syntax highlighting -->
<link href="https://cdnjs.cloudflare.com/ajax/libs/prism-themes/1.9.0/prism-vs.min.css" rel="stylesheet" />

<!-- Mermaid.js for clean flowcharts / diagrams -->
<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true, theme: 'default' });
</script>
```
*Note: Use `\\[` and `\\]` for block math equations.*

---

## 6. Diagram & Example Simplicity (Critical User Requirement)
- **Zero Cryptic Abbreviations**: Do NOT overcomplicate examples or diagrams with obscure codes or cryptic IDs.
- **Intuitive Real-World Entities**: Use natural, recognizable entities (e.g. Pune landmarks like *Shaniwar Wada*, *Aga Khan Palace*, *Sinhagad Fort*, *Fergusson College*, *Koregaon Park*; or standard intuitive state spaces like Exam Scheduling, Medical Diagnosis, Robot Navigation).
- **Handcrafted Clean SVGs**: Prefer crisp, handcrafted SVG diagrams or clean Mermaid charts over tangled, automatic force-directed diagrams with crossed lines.
- **Immediately Legible**: Ensure all diagrams, nodes, and states are visually engaging, modern, and self-explanatory.

---

## 7. Standard Academic Section Structure (AIML Assignments)
Modeled directly after the high-scoring DAA Assignment 6 structure, every AIML assignment report follows this 17-section structure:

1. **1. Aim**
2. **2. Problem Statement**
3. **3. Objective**
4. **4. Introduction** (Background, AI paradigm, problem context)
5. **5. Theory & Formulation** (State space formulation, heuristic/loss definitions, recurrence equations, search bounds, algorithm pseudocode)
6. **6. Example Walkthrough** (Practical real-world scenario with clean data tables, diagrams, and step-by-step state trace)
7. **7. Python Program** (Structured in clean Part 1 & Part 2 `.code-window-light` blocks)
8. **8. OUTPUT** (Authentic PowerShell terminal window with realistic commands `python ...` and execution logs)
9. **9. Implementation Details** (Architecture, data structures, hyperparameters, state encoding)
10. **10. Time Complexity Analysis** (Branching factors, depth, theoretical Big-O derivations)
11. **11. Space Complexity Analysis** (Frontier size, visited sets, memory bounds)
12. **12. Comparison of Approaches / Heuristics / Algorithms**
13. **13. Advantages**
14. **14. Limitations**
15. **15. Applications**
16. **16. Result**
17. **17. Conclusion**

---

## 8. The Gold-Standard 7-Page Architecture Standard
To eliminate awkward page breaks, avoid cut-off sections, prevent orphan subheadings from appearing at the top of pages, and ensure reports do not sprawl across 9–10 pages, every AIML report must strictly adhere to this exact **7-Page Distribution** established in DAA Assignment 6:

- **Page 1**: Cover Metadata Table + `<h2>1. Aim</h2>` + `<h2>2. Problem Statement</h2>` + `<h2>3. Objective</h2>`.
- **Page 2**: `<h2>4. Introduction</h2>` + `<h2>5. Theory & Formulation</h2>` (Mathematical definitions, state representation, heuristic function properties, admissibility/consistency, algorithm pseudocode).
- **Page 3**: `<h2>6. Example Walkthrough</h2>` (**100% SELF-CONTAINED on Page 3**: initial state table, clean handcrafted SVG diagram / state graph, step-by-step search trace table, and optimal path/solution summary. Zero spillovers to other pages!).
- **Page 4**: `<h2>7. Python Program (Part 1)</h2>` (State representations, heuristic evaluators, core AI search/learning algorithm in a clean `.code-window-light`).
- **Page 5**: `<h2>7. Python Program (Part 2)</h2>` (Pipeline driver / benchmark runner) + `<h2>8. OUTPUT</h2>` (Authentic PowerShell terminal console, ~20–25 lines) + `<h2>9. Implementation Details</h2>`.
- **Page 6**: `<h2>10. Time Complexity Analysis</h2>` + `<h2>11. Space Complexity Analysis</h2>` + `<h2>12. Comparison Table</h2>`.
- **Page 7**: `<h2>13. Advantages</h2>` + `<h2>14. Limitations</h2>` + `<h2>15. Applications</h2>` + `<h2>16. Result</h2>` + `<h2>17. Conclusion</h2>`.

### Critical Page Rules:
1. **Always Begin with `<h2>`**: Every page (from Page 2 to Page 7) MUST start with an `<h2>` heading at the very top. Never permit an orphan `<h3>`, isolated table, or loose paragraph to begin a page.
2. **Page 3 Self-Containment**: The Example Walkthrough must be fully contained on Page 3. Size tables and diagrams so the entire walkthrough begins and finishes on Page 3.
3. **Dense & Balanced Packing**: No large white gaps at the bottom of pages, and no overflowing beyond the 11-inch boundary on screen.
