#!/usr/bin/env python3.11

import argparse


parser = argparse.ArgumentParser(
		prog="Log file reader",
		description="Reads data from log file")

parser.add_argument('filename', type=str, help="Enter the log file name")

args = parser.parse_args()
input_file = args.filename

f = open(input_file)
count = 0

product_names = ["Mozilla", "Gecko", "AppleWebKit",
		 "Safari", "Mobile Safari", "Mobile",
		 "Chrome"]

user_agents = []

while True:
	count+=1

	line = f.readline()
	log = line.strip()


	check = "Mozilla/5.0" in log

	if check is True:

		x = log.split("Mozilla/5.0")
		user_agents+= [x[1]]

	if not line:
		break

user_agents2 = user_agents
user_agents = list( dict.fromkeys(user_agents) )

print("STATISTICS")

for agent in user_agents:

	print(f"USER AGENT: {agent}")
	print(f"Number of requests: {user_agents2.count(agent)}")


#FUNCTION TO PRINT NUMBER OF REQUESTS FROM USERAGENTS







