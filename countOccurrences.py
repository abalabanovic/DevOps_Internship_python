#!/usr/bin/env python3.11

import argparse

parser = argparse.ArgumentParser(
	prog='Count Occurrences',
	description='count occurrences for all charachters')

parser.add_argument('filename', type=str, help="Input string")
args = parser.parse_args()
input_string = args.filename

check = []
final_print = ""

for char in input_string:

	if char in check:
		continue

	print(f"{char}:{input_string.count(char)}, ", end="")
	check+=char

