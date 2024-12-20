# PDF Splitter and Merger

**PDF Splitter and Merger** is a Python-based command-line tool for splitting and merging PDF files. It simplifies document management with quick and efficient operations.

## Features
- **Split PDFs**: Split a PDF file into individual pages.
- **Merge PDFs**: Combine multiple PDF files into one.
- **Easy CLI**: Simple commands for flexible input and output.

## Installation

1. Clone the repository:
```bash
   git clone https://github.com/LF3551/PDF-Splitter-and-Merger.git
   cd PDFSplitterMerger
 ```

2. Install the required dependencies:
```bash
   pip install -r requirements.txt
 ```

 ### Commands

#### Split a PDF
Split a PDF into individual pages:
```bash
python3 main.py split --input=test.pdf --output=output_folder
```

#### Merge PDFs
Combine multiple PDFs into one:
```bash
python3 main.py merge --input output_folder/*.pdf --output merged.pdf
```
