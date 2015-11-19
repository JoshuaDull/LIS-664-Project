import json 
import csv

artist_dict = {}


with open ("1931_1948_2.csv", "r") as in_file:
	data = csv.reader(in_file)
	for row in data:
		object_no = row[0]
		artist_name = row[3]
		title = row[5]
		classification = row[2]
		date = row[6]
		medium = row[8]
		dimensions = row[9]
		credit = row[11]
		if artist_name not in artist_dict:
			artist_dict[artist_name] = {} #dictionary for each artist by name
			artist_dict[artist_name]['OBJECTS'] = {}
			artist_dict[artist_name]['BIOGRAPHIC'] = {}
		if object_no not in artist_dict[artist_name]['OBJECTS']:
			artist_dict[artist_name]['OBJECTS'][object_no] = {} #create dicitonary for each object
			artist_dict[artist_name]['OBJECTS'][object_no]['TITLE'] = title
			artist_dict[artist_name]['OBJECTS'][object_no]['CLASS'] = classification
			artist_dict[artist_name]['OBJECTS'][object_no]['DATE'] = date
			artist_dict[artist_name]['OBJECTS'][object_no]['MEDIUM'] = medium
			artist_dict[artist_name]['OBJECTS'][object_no]['DIMENSIONS'] = dimensions
			artist_dict[artist_name]['OBJECTS'][object_no]['CREDIT_LINE'] = credit

with open ("death_info.csv", "r") as in_file:
	data = csv.reader(in_file)
	for row in data:
		artist_name = row[2]
		death_year = row[4]
		city = row[6]
		state = row[7]
		country = row[8]
		latitude = row[]
		longitude = row[]
		geonameID = row[]
		if artist_name in artist_dict:
			artist_dict[artist_name]['BIOGRAPHIC']['DEATH'] = {}
			artist_dict[artist_name]['BIOGRAPHIC']['DEATH']['YEAR'] = death_year
			artist_dict[artist_name]['BIOGRAPHIC']['DEATH']['CITY'] = city
			artist_dict[artist_name]['BIOGRAPHIC']['DEATH']['STATE'] = state
			artist_dict[artist_name]['BIOGRAPHIC']['DEATH']['COUNTRY'] = country
			artist_dict[artist_name]['BIOGRAPHIC']['DEATH']['LATITUDE'] = latitude
			artist_dict[artist_name]['BIOGRAPHIC']['DEATH']['LONGITUDE'] = longitude
			artist_dict[artist_name]['BIOGRAPHIC']['DEATH']['geonameID'] = geonameID

with open ("birth_info.csv", "r") as in_file:
	data = csv.reader(in_file)
	for row in data:
		artist_name = row[2]
		birth_year = row[3]
		city = row[6]
		state = row[7]
		country = row[8]
		latitude = row[]
		longitude = row[]
		geonameID = row[]
		if artist_name in artist_dict:
			artist_dict[artist_name]['BIOGRAPHIC']['BIRTH'] = {}	
			artist_dict[artist_name]['BIOGRAPHIC']['BIRTH']['YEAR'] = birth_year
			artist_dict[artist_name]['BIOGRAPHIC']['BIRTH']['CITY'] = city
			artist_dict[artist_name]['BIOGRAPHIC']['BIRTH']['STATE'] = state
			artist_dict[artist_name]['BIOGRAPHIC']['BIRTH']['COUNTRY'] = country
			artist_dict[artist_name]['BIOGRAPHIC']['BIRTH']['LATITUDE'] = latitude
			artist_dict[artist_name]['BIOGRAPHIC']['BIRTH']['LONGITUDE'] = longitude
			artist_dict[artist_name]['BIOGRAPHIC']['BIRTH']['geonameID'] = geonameID


			
with open('project_data.json', 'w') as out_file:
	json.dump(artist_dict, out_file)
			
		
