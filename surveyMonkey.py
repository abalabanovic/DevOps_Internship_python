#!/usr/bin/env python3.11

import argparse
import json
import requests

parser = argparse.ArgumentParser(
				prog='Survey monkey 1.0',
				description="Working with SM API and json")


parser.add_argument('filename', help = "Provide json file for survey")
parser.add_argument('-e', '--email', type=str)
args = parser.parse_args()

json_file = args.filename
email_file = args.email

access_token = 'cOmUpOXfevWx560egh1njmf5pFwFlZFmf5zGe.mlDlE9g43C6F-3hmIBR4M-ciKOwdUTWpwZlQTTbgXGhlABdQxGNBX1hGHxKjJfq9psGXwxzXmilvZC35jeWAJTRXkz'


with open(json_file, 'r') as f:
	data_json = json.load(f)

headers = {

	'Authorization': f'Bearer {access_token}',
	'Content-Type': 'application/json'

}


response = requests.post('https://api.surveymonkey.com/v3/surveys', json=data_json, headers=headers)

if response.status_code == 201:
	survey_id = response.json()['id']
	survey_link = f'https://www.surveymonkey.com/r/{survey_id}'

else:
	print(f"Failed to create survey : {response.text}")

"""

for page in data['pages']:


	for question in page['questions']:

		question_text = question['question_text']
		question_type = question['question_type']
		choices = question.get('choices', [])

		if question_type == 'multiple_choice':

			print("MC")

"""

print("Survey created sucessfully")
print(survey_link)
