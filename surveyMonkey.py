#!/usr/bin/env python3.11

import argparse

parser = argparse.ArgumentParser(
				prog='Survey monkey 1.0',
				description="Working with SM API and json")


parser.add_argument('filename', help = "Provide json file for survey")
parser.add_argument('-e', '--email', type=str)
args = parser.parse_args()

json_file = args.filename
email_file = args.email

# Getting emails from a file

emails = []



