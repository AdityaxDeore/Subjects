# PCCOE Assignment Design & Layout Specification

This document serves as the absolute source of truth for generating, styling, and formatting assignments for PCCOE. Any AI assisting with creating or editing assignments must strictly adhere to these rules to ensure the exact visual presentation the user expects.

## 1. Core Architecture
- **HTML Structure**: Assignments are built as single HTML files.
- **Visual Page Cuts**: The document is NOT a single continuous white block. It must be broken down into individual `<div class="page">` blocks to simulate physical paper on the screen.
- **Editable Mode**: The main container must have `contenteditable="true"` so the user can click and type or paste screenshots directly into their browser before printing.
- **No Footers**: There are strictly NO footers (`.page-footer`, `.print-footer`, etc.). Do not generate them.

## 2. Page Dimensions & Dual-Padding System
This is the most critical feature. The assignment must look like a beautifully padded document on screen, but must print efficiently to save paper.

### Screen CSS (The "Preview")
```css
body {
  font-family: Arial, sans-serif;
  font-size: 12pt;
  line-height: 1.5;
  color: #000;
  background: #e5e7eb; /* Grey background outside the pages */
  padding: 20px;
}

.container {
  max-width: 8.5in;
  margin: 0 auto;
}

.page {
  min-height: 11in;
  width: 8.5in;
  padding: 0.8in; /* Wide, beautiful margins for the screen preview */
  background: #ffffff;
  margin: 0 auto 20px auto;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  position: relative;
}
.page:focus-within {
  outline: 2px dashed #4299e1; /* Shows when user is editing */
}
```

### Print CSS (`@media print` & `@page`)
To completely eliminate browser-generated default headers (URL, webpage title) and footers (date, page numbers), the CSS `@page` rule must have `margin: 0`. The actual physical margins on paper are then cleanly provided via internal padding on `.page`:

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
  pre, code {
    white-space: pre-wrap !important;
    word-break: break-all !important;
  }
  h2, h3 {
    page-break-after: avoid !important;
    break-after: avoid !important;
  }
  .styled-table, .cover-table, .diagram-container, 
  .code-window-light, .terminal-window, .math-callout, .algo-container {
    page-break-inside: avoid !important;
    break-inside: avoid !important;
  }
  li {
    page-break-inside: avoid !important;
    break-inside: avoid !important;
  }
}
```

## 3. Cover Page Table
Every assignment must begin with this exact structured metadata table inside the first `.page`.
- Font: `Times New Roman`
- Borders: `1px solid #000`
- Logo width: 18% of the table.

**HTML Template:**
```html
<table class="cover-table">
  <tr>
    <td class="logo-container">
      <img src="pccoelogo.jfif" alt="PCCOE Logo" contenteditable="false">
    </td>
    <td class="college-info">
      Pimpri Chinchwad Education Trust's<br>
      Pimpri Chinchwad college of Engineering
    </td>
  </tr>
  <tr>
    <td colspan="2" class="row-centered">
      Assignment No.[X]
    </td>
  </tr>
  <tr>
    <td colspan="2" class="row-left">
      Course:- [Course Name]
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
</table>
```
**Cover Table CSS:**
```css
.cover-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 25px;
  font-family: 'Times New Roman', Times, serif;
}
.cover-table td {
  border: 1px solid #000;
  padding: 8px 12px;
}
.cover-table .college-info {
  text-align: center;
  font-weight: bold;
  font-size: 16pt;
  line-height: 1.4;
}
.cover-table .row-centered { text-align: center; font-weight: bold; font-size: 14pt; }
.cover-table .row-left { text-align: left; font-weight: bold; font-size: 14pt; }
.logo-container { text-align: center; width: 18%; padding: 5px !important; }
.logo-container img { max-width: 100px; height: auto; display: block; margin: 0 auto; }
```

## 4. Typography & Elements
- **Headings (`h2`)**: `Arial`, `16pt`, `color: #000`, `margin-top: 25px`, `margin-bottom: 10px`.
- **Subheadings (`h3`)**: `Arial`, `14pt`, `color: #000`, `margin-top: 18px`, `margin-bottom: 10px`.
- **Paragraphs (`p`)**: `Arial`, `11pt`, `text-align: justify`, `line-height: 1.5`, `margin-bottom: 15px`.
- **Lists (`ul`, `ol`)**: `margin-left: 20px`, `11pt`.
- **Code Blocks (`pre`)**: `background-color: #f8f9fa`, `border: 1px solid #ccc`, `font-size: 10pt`, `padding: 10px`.
- **Data Tables (`.styled-table`)**: `100% width`, `border-collapse: collapse`. Cells have `1px solid #000` and `padding: 8px`. Header (`th`) has `background-color: #f2f2f2`.

## 5. External Libraries
Always include MathJax in the `<head>` for rendering mathematical formulas:
```html
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
```
*Note: Use `\\[` and `\\]` for block math equations.*

## 6. AI Instruction: Manual Page Balancing
Because the document is broken into manual `<div class="page">` chunks to provide the visual grey gaps on the screen preview, **the AI must carefully pack the text.**
- Do not let pages run on for too long, or the text will overflow the 11-inch box on screen.
- Do not leave massive white gaps at the bottom of the pages. Combine sections or move text up to ensure the pages are densely packed and well-balanced.
- Remember that the screen padding is `0.7in-0.8in`, meaning the printable height on screen is smaller than the actual paper. Distribute the content thoughtfully!

## 7. Standard Academic Section Structure (Assignments 6, 7, 8)
Every DAA laboratory report follows this exact 17-section structure:
1. **1. Aim**
2. **2. Problem Statement**
3. **3. Objective**
4. **4. Introduction**
5. **5. Theory** (Mathematical formulation, bounds, recurrence relations, and formal pseudocode algorithms)
6. **6. Example** (Practical real-world scenario with clean data tables, diagrams, and step-by-step trace)
7. **7. Java Program** (Structured in clean Part 1 & Part 2 `.code-window-light` blocks)
8. **8. OUTPUT** (Authentic terminal window with realistic commands and execution logs)
9. **9. Implementation Details**
10. **10. Time Complexity Analysis**
11. **11. Space Complexity Analysis**
12. **12. Comparison of Different Implementations / Approaches**
13. **13. Advantages**
14. **14. Limitations**
15. **15. Applications**
16. **16. Result**
17. **17. Conclusion**

## 8. Diagram & Example Simplicity (Critical User Requirement)
- **Do NOT overcomplicate examples or diagrams with cryptic codes** (e.g. avoid `OE32`, `DS305`, `IXU`, `BOM`, etc.).
- Use simple, natural, intuitive entities (e.g. subjects like *Mathematics*, *Physics*, *Computer Science*, *Chemistry*, *Electronics*, *Humanities*; or cities like *Pune*, *Mumbai*, *Nashik*, *Aurangabad*, *Kolhapur*).
- Prefer **handcrafted, clean, crisp SVG diagrams** or simple, well-structured tree/network visuals over messy automatic force-directed diagrams with tangled crossing lines.
- Ensure diagrams are visually engaging, modern, and immediately self-explanatory.

## 9. Authentic Console Terminal Windows
- Background: `#0c0c0c` or `#1e222a` (dark, realistic terminal).
- Text color: Standard console gray `#cccccc` or `#abb2bf`.
- Prompts: Realistic Windows PowerShell prompt `PS C:\Users\adity\Desktop\Subjects\DAA\...>` with `javac` and `java` commands.
- **Zero neon/fluorescent spans**: Avoid harsh cyan/green text highlights. Keep the terminal looking like an authentic engineering console.

## 10. Suppression of Browser Headers and Footers on Print
- By setting `@page { margin: 0; }`, the browser's automatic headers (title, page URL) and footers (date, "1/X") are completely hidden.
- The document margins on physical paper are provided by internal `.page` padding: `padding: 12mm 15mm !important;`.
- Ensure `page-break-after: always !important;` on `.page` so each page prints onto its own physical A4 sheet.

## 11. The Gold-Standard 7-Page Architecture Standard
To prevent content from being cut across page breaks, orphan subheadings appearing at the top of pages, or reports sprawling across 9–10 pages, every DAA assignment report must strictly adhere to this exact 7-page distribution modeled after Assignment 6:

- **Page 1**: Cover Metadata Table + `<h2>1. Aim</h2>` + `<h2>2. Problem Statement</h2>` + `<h2>3. Objective</h2>`.
- **Page 2**: `<h2>4. Introduction</h2>` + `<h2>5. Theory</h2>` (Mathematical formulations, bounds, theorems, algorithmic concepts, and theoretical comparison tables).
- **Page 3**: `<h2>6. Example Walkthrough</h2>` (**100% SELF-CONTAINED on Page 3**: initial problem table, clean handcrafted SVG diagram, step-by-step trace table, and optimal manifest summary. Zero spillovers or cuts to next pages!).
- **Page 4**: `<h2>7. Java Program (Part 1)</h2>` (Data models, helper structures, and core reduction/coloring algorithm in a clean `.code-window-light`).
- **Page 5**: `<h2>7. Java Program (Part 2)</h2>` (Search engine/runner) + `<h2>8. OUTPUT</h2>` (Authentic PowerShell console window, ~20–25 lines) + `<h2>9. Implementation Details</h2>`.
- **Page 6**: `<h2>10. Time Complexity Analysis</h2>` + `<h2>11. Space Complexity Analysis</h2>` + `<h2>12. Comparison Table</h2>`.
- **Page 7**: `<h2>13. Advantages</h2>` + `<h2>14. Limitations</h2>` + `<h2>15. Applications</h2>` + `<h2>16. Result</h2>` + `<h2>17. Conclusion</h2>`.

Every page must start with an `<h2>` heading (except Page 1 which starts with the cover table). Never allow an orphan `<h3>` or table to start at the very top of a page.

