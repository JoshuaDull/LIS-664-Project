import csv
import json

def whoAreYou(artistName):
	with open ("artist_data.json", "r") as in_file:
	data = json.load(in_file)
	for row in data:
		if artistName in data[row]:
			dob = data[row]['BIOGRAPHIC']['BIRTH']['YEAR']
			dod = data[row]['BIOGRAPHIC']['DEATH']['YEAR']
			country = data[row]['BIOGRAPHIC']['BIRTH']['COUNTRY']
			countryTwo = data[row]['BIOGRAPHIC']['DEATH']['COUNTRY']
			print(artistName + "was born in the year " + dob + " in " + country)
			print(artistName + "died in the year " + dod + " in " + countryTwo)
		elif:
			print("Artist not found")