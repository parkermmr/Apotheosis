---
title: "Document Template"
author: ""       
date: ""               
geometry:
  - top=1in
  - bottom=1in
  - left=1in
  - right=1in
toc: true
toc-title: "Table of Contents"
---

<style>
@page {
    /* Red name in top-center and bottom-center of each page */
    @top-center {
        content: "Name"; 
        font-size: 12pt;
        font-weight: bold;
        color: red;
    }
    @bottom-center {
        content: "Name";
        font-size: 12pt;
        font-weight: bold;
        color: red;
    }
    @bottom-right {
        content: "Page " counter(page);
        font-size: 10pt;
        color: black;
    }
    size: A4;
    margin: 1in;
}

body {
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;
    position: relative;
}

/* Red 'DRAFT' watermark */
.watermark {
    position: fixed;
    top: 35%;
    left: 10%;
    width: 80%;
    text-align: center;
    font-size: 80px;
    font-weight: bold;
    color: rgba(255, 0, 0, 0.1);
    transform: rotate(-30deg);
    z-index: -1;
    pointer-events: none;
}

/* Main title styling */
.headerTitle {
  font-size: 45px;
  text-align: center;
}

.tab {
  display: inline-block;
  margin-left: 40px;
}

/* Utility class for screen-reader only content */
.visually-hidden {
    clip: rect(0 0 0 0);
    clip-path: inset(100%);
    height: 1px;
    overflow: hidden;
    position: absolute;
    width: 1px;
    white-space: nowrap;
}

/* Table of Contents styling */
.toc-list, .toc-list ol {
  list-style-type: none;
  padding: 0;
}
.toc-list ol {
  /* Force alphabetical for nested items */
  list-style-type: lower-alpha;
  padding-inline-start: 2ch;
}
.toc-list > li > a {
  font-weight: bold;
  margin-block-start: 1em;
}
.toc-list li > a {
    text-decoration: none;
    display: grid;
    grid-template-columns: auto max-content;
    align-items: end;
}
.toc-list li > a > .title {
    position: relative;
    overflow: hidden;
}
.toc-list li > a .leaders::after {
    position: absolute;
    padding-inline-start: .25ch;
    content: " . . . . . . . . . . . . . . . . . . . "
        ". . . . . . . . . . . . . . . . . . . . . . . "
        ". . . . . . . . . . . . . . . . . . . . . . . "
        ". . . . . . . . . . . . . . . . . . . . . . . "
        ". . . . . . . . . . . . . . . . . . . . . . . "
        ". . . . . . . . . . . . . . . . . . . . . . . "
        ". . . . . . . . . . . . . . . . . . . . . . . ";
    text-align: right;
}

/* Version control table styling */
.version-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 10px;
    margin-bottom: 20px;
}
.version-table th, .version-table td {
    border: 1px solid #ccc;
    padding: 8px;
    text-align: left;
}
.version-table th {
    background-color: #f2f2f2;
}
</style>

<!-- Red DRAFT watermark -->
<div class="watermark">DRAFT</div>

<!-- Main Document Title -->
<h1 class="headerTitle">Report Document Template</h1>

<!-- Author / Date lines; replace if needed -->
### Author: Name  
### Date: 29/02/2020  

---

<h2>Document Version Control</h2>
<table class="version-table">
<tr>
    <th>Version</th>
    <th>Date</th>
    <th>Author</th>
    <th>Change Description</th>
</tr>
<tr>
    <td>1.0</td>
    <td>2024-01-01</td>
    <td>MYNAME</td>
    <td>Initial Draft</td>
</tr>
<tr>
    <td>1.1</td>
    <td>2024-02-15</td>
    <td>MYNAME</td>
    <td>Updated with review comments</td>
</tr>
<tr>
    <td>1.2</td>
    <td>2024-03-05</td>
    <td>MYNAME</td>
    <td>Finalized</td>
</tr>
</table>

---

<h2>Table of Contents</h2>
<ol class="toc-list" role="list">
  <li>
    <a href="#Introduction">
      <span class="title">1. Introduction<span class="leaders" aria-hidden="true"></span></span>
    </a>
    <ol role="list">
      <li>
        <a href="#Background">
          <span class="title">Background<span class="leaders" aria-hidden="true"></span></span>
        </a>
      </li>
      <li>
        <a href="#Scope">
          <span class="title">Scope<span class="leaders" aria-hidden="true"></span></span>
        </a>
      </li>
    </ol>
  </li>
  <li>
    <a href="#Methodology">
      <span class="title">2. Methodology<span class="leaders" aria-hidden="true"></span></span>
    </a>
    <ol role="list">
      <li>
        <a href="#DataCollection">
          <span class="title">Data Collection<span class="leaders" aria-hidden="true"></span></span>
        </a>
      </li>
      <li>
        <a href="#Analysis">
          <span class="title">Analysis<span class="leaders" aria-hidden="true"></span></span>
        </a>
      </li>
    </ol>
  </li>
  <li>
    <a href="#Conclusion">
      <span class="title">3. Conclusion<span class="leaders" aria-hidden="true"></span></span>
    </a>
  </li>
</ol>

---

<!-- Main content sections matching the TOC -->
<h3 id="Introduction">1. Introduction</h3>

<h4 id="Background">Background</h4>
<p>[Your background content here]</p>

<h4 id="Scope">Scope</h4>
<p>[Your scope content here]</p>

<h3 id="Methodology">2. Methodology</h3>

<h4 id="DataCollection">Data Collection</h4>
<p>[Your data collection info here]</p>

<h4 id="Analysis">Analysis</h4>
<p>[Your analysis info here]</p>

<h3 id="Conclusion">3. Conclusion</h3>
<p>[Your conclusion here]</p>
