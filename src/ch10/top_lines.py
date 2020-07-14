"""Using `argparse` module to parse command line arguments."""

import argparse

parser = argparse.ArgumentParser(
    prog="top_lines", description="Show top lines from each file"
)
parser.add_argument("filenames", nargs="+")
parser.add_argument("-l", "--lines", type=int, default=10)
args: argparse.Namespace = parser.parse_args()
print(args)
