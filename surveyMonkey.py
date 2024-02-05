#!/usr/bin/env python3.11

import argparse
import json

parser = argparse.ArgumentParser(
				prog='Survey monkey 1.0',
				description="Working with SM API and json")


parser.add_argument('filename', help = "Provide json file for survey")
parser.add_argument('-e', '--email', type=str)
args = parser.parse_args()

json_file = args.filename
email_file = args.email

#client = Client('Your_Access_token')


with open(json_file, 'r') as f:
	data = json.load(f)

#survey = client.create_survey(data['title'])


for page in data['pages']:

	#page_id = survey.create_page(page['title']).id

	for question in page['questions']:

		question_text = question['question_text']
		question_type = question['question_type']
		choices = question.get('choices', [])

		if question_type == 'multiple_choice':

			print("MC")
			#survey.create_question(page_id, question_text, 'multiple_choice', choices=choices)

# survey.finalize()
# survey_link = survey.collectors[0].url

print("Survey created sucessfully")


