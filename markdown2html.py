#!/usr/bin/python3
"""
   Parsing bold syntax
"""
if __name__ == "__main__":
    import sys
    from os import path
    
if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)
mark_file = sys.argv[1]
output_file = sys.argv[2]
if not os.path.isfile(markdown_file):
    print("Missing {}".format(markdown_file), file=sys.stderr)
    sys.exit(1)
sys.exit(0)
