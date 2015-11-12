import csv
import json

def whoAreYou(artistName):
	with open ("project_data.json", "r") as in_file:
	  data = json.load(in_file)
	  for row in data:
	    if artistName in row:
	      dob = data[row]['BIOGRAPHIC']['BIRTH']['YEAR']
	      dod = data[row]['BIOGRAPHIC']['DEATH']['YEAR']
	      country = data[row]['BIOGRAPHIC']['BIRTH']['COUNTRY']
	      countryTwo = data[row]['BIOGRAPHIC']['DEATH']['COUNTRY']
	      print(artistName + " was born in the year " + dob + " in " + country + '.')
	      print(artistName + " died in the year " + dod + " in " + countryTwo + '.')



whoAreYou('Emma Lu Davis')
whoAreYou('Man Ray')