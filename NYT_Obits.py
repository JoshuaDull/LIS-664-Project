import requests
import json
import csv

with open("deathInformation.csv", "r") as in_file, open("obits.csv", "w") as out_file:
	x = csv.reader(in_file)
	w = csv.writer(out_file)
	row0 = next(x)
	row0.append('NYT_URL')
	w.writerow(row0)
	for row in x:
		artist_name = row[2]
		date1 = int(row[4] + '0101')
		date2 = int(row[4] + '1231')
		payload = { 'q' : artist_name, 'fq' : "type_of_material.contains:(Obituary)", 'begin_date': date1, 'end_date': date2, 'api-key': "86e35586ca628b7b5577029c151f825c:17:72915474" }
		r = requests.get("http://api.nytimes.com/svc/search/v2/articlesearch.json", params = payload)
		data = json.loads(r.text)
		try:
			row.append(data['response']['docs'][0]['web_url'])
			w.writerow(row)
		except:
			w.writerow(row)
			continue