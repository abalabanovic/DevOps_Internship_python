#!/usr/bin/env python3.11

import argparse
import os

parser = argparse.ArgumentParser(
		prog='System Info',
		description='Gives information about system')

parser.add_argument('-u', '--user', action='store_true')
parser.add_argument('-m', '--memory', action='store_true')
parser.add_argument('-c', '--cpu', action='store_true')
parser.add_argument('-i', '--ip', action='store_true')
parser.add_argument('-d', '--distro', action='store_true')
parser.add_argument('-l', '--load', action = 'store_true')
arg = parser.parse_args()

flag_u = arg.user
flag_m = arg.memory
flag_c = arg.cpu
flag_i = arg.ip
flag_d = arg.distro
flag_l = arg.load

if flag_u is True:

	user = os.environ["USER"]
	print(f"User : {user}")
	os.system('cat /etc/passwd | grep $USER')
	print("\n")

if flag_i is True:

	print("Private IP address:")
	os.system('hostname -I')

	print("Public IP address:")
	test=os.system('curl ifconfig.me')
	print("\n")

	# IF CURL IS NOT INSTALLED

	"""
	test=os.system(var=$('curl --version'))


	if test == 0:

		print("Public IP address")
		os.system('curl ifconfig.me')
		print("\n")

	else:

		print("Public IP not available, please install curl!")
		answer = input("Do you want to install curl[y/n]\n")

		if answer == 'y':

			os.system('sudo apt install curl -y')
			print("Public IP address")
			os.system('curl ifconfig.me')
			print("\n")

	"""

if flag_d is True:

	print("Linux distribution:")
	os.system('uname -srm')
	print("\n")


if flag_c is True:


	print("CPU info:")
	os.system('cat /proc/cpuinfo | grep "vendor" | uniq')
	os.system('cat /proc/cpuinfo | grep "model name" | uniq')
	os.system('cat /proc/cpuinfo | grep "core id"')
	print("\n")

if flag_l is True:

	print("Load balance:")
	os.system('cat /proc/loadavg')
	print("\n")

if flag_m is True:

	print("Memory info:")
	os.system('free -h')

