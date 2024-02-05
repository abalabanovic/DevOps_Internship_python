#!/usr/bin/env python3.11

import argparse

parser = argparse.ArgumentParser(
		prog="Create Tuple",
		description="Find minimum and maximum from list")


parser.add_argument('--numbers', "-n", nargs="+", type=int, help="For example -n 1 2 3 4")

args = parser.parse_args()
list_int = args.numbers

list_int = list( dict.fromkeys(list_int) )

my_tuple = tuple(list_int)

print(f"Maximum is {max(my_tuple)}")
print(f"Minimum is {min(my_tuple)}")
