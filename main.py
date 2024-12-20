
"""
Copyright (c) 2024 Aleksei Aleinikov

Licensed under the Universal Permissive License (UPL), Version 1.0.
You may obtain a copy of the License at https://opensource.org/licenses/UPL

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software, associated documentation and/or data (collectively the
"Software"), to deal in the Software without restriction, including without
limitation the rights to copy, create derivative works of, display, perform,
and distribute the Software and make, use, sell, offer for sale, import,
export, have made, and have sold the Software and the Larger Work(s), and to
sublicense the foregoing rights on either these or other terms.

This license is subject to the following condition:
The above copyright notice and this permission notice must be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import argparse
from PyPDF2 import PdfReader, PdfWriter
import os

def split_pdf(input_file, output_folder):
    try:
        reader = PdfReader(input_file)
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for i, page in enumerate(reader.pages):
            writer = PdfWriter()
            writer.add_page(page)
            output_path = os.path.join(output_folder, f"page_{i + 1}.pdf")
            with open(output_path, 'wb') as output_pdf:
                writer.write(output_pdf)

        print(f"Successfully split {input_file} into {len(reader.pages)} pages in {output_folder}.")
    except Exception as e:
        print(f"Error splitting PDF: {e}")

def merge_pdfs(input_files, output_file):
    try:
        writer = PdfWriter()
        for file in input_files:
            reader = PdfReader(file)
            for page in reader.pages:
                writer.add_page(page)

        with open(output_file, 'wb') as output_pdf:
            writer.write(output_pdf)

        print(f"Successfully merged {len(input_files)} PDFs into {output_file}.")
    except Exception as e:
        print(f"Error merging PDFs: {e}")

def main():
    parser = argparse.ArgumentParser(description="PDF Splitter and Merger Tool")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")


    split_parser = subparsers.add_parser('split', help="Split a PDF into individual pages")
    split_parser.add_argument('--input', '-i', required=True, help="Input PDF file")
    split_parser.add_argument('--output', '-o', required=True, help="Output folder for split PDFs")


    merge_parser = subparsers.add_parser('merge', help="Merge multiple PDFs into a single file")
    merge_parser.add_argument('--input', '-i', nargs='+', required=True, help="List of input PDF files")
    merge_parser.add_argument('--output', '-o', required=True, help="Output merged PDF file")

    args = parser.parse_args()

    if args.command == 'split':
        split_pdf(args.input, args.output)
    elif args.command == 'merge':
        merge_pdfs(args.input, args.output)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

    