#!/usr/bin/python
import sys
import os
"""
markdown2html.py

This script converts a Markdown file to an HTML file.
Arguments:
    input_markdown_file: The path to the input Markdown (.md) file.
    output_html_file: The path to the output HTML (.html) file.
"""
if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)
mark_file = sys.argv[1]
output_file = sys.argv[2]
if not os.path.isfile(markdown_file):
    print("Missing {}".format(markdown_file), file=sys.stderr)
    sys.exit(1)
sys.exit(0)
