import os
import argparse
from .markdown_merger import MarkdownMerger

def main():
    merger = MarkdownMerger()

    parser = argparse.ArgumentParser(description="Merge markdown files.")
    parser.add_argument("-f", "--files", nargs="+", help="Markdown files to merge.")
    parser.add_argument("-d", "--dir", help="Directory containing markdown files to merge.")
    parser.add_argument("-e", "--exclude", nargs="+", help="Files to exclude from merging.")
    parser.add_argument("-o", "--output", help="Output file name.")
    args = parser.parse_args()

    _files = args.files
    _dir = args.dir
    _excludes = args.exclude
    _output = args.output

    if _files is None and _dir is None:
        print("No files or path provided.")
        return
    elif _files:
        for file in _files:
            with open(file, "r") as f:
                merger.feed(f.read())
    elif _dir:
        for root, _, files in sorted(os.walk(_dir)):
            for file in sorted(files):
                ext = os.path.splitext(file)[1]
                if ext not in [".md", ".markdown"]:
                    continue
                if _excludes and file in _excludes:
                    continue
                with open(os.path.join(root, file), "r") as f:
                    merger.feed(f.read())

    if _output:
        with open(_output, "w") as f:
            f.write(merger.out())
    else:
        print(merger.out())

if __name__ == "__main__":
    main()
