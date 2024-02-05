#!/usr/bin/env python3.11

import argparse
import sys

parser = argparse.ArgumentParser(
		prog='Extension',
		description='Puts extension to outpu')

parser.add_argument('filename', help="The file to read")

args = parser.parse_args()
file = args.filename

try:

	x = file.split(".")
	print(x[1])

except:

	print("File does not have extension")
	sys.exit(1)



