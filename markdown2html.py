#!/usr/bin/python3
""" Module for markdown2html.py"""
import sys
import os
"""
 Check if the number of arguments is less than 2
 Get the input and output filenames from the arguments
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
