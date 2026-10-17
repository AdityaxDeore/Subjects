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

### Print CSS (`@media print`)
```css
@media print {
  body {
    background: #ffffff;
    padding: 0;
  }
  .container {
    max-width: 100%;
    margin: 0;
    box-shadow: none;
  }
  .page {
    width: 100%;
    min-height: auto;
    margin: 0;
    padding: 0.2in; /* Thinner padding specifically for printing to save space */
    box-shadow: none;
    border: none;
    page-break-after: always;
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
- Remember that the screen padding is `0.8in`, meaning the printable height on screen is smaller than the actual paper. Distribute the content thoughtfully!
