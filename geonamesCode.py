import json
import requests
import csv

geonamesbirth = {}
geonamesdeath = {}

with open("birthGeo.csv", "r") as in_file, open("birthGeonames.csv", "w") as out_file:
    x = csv.reader(in_file)
    w = csv.writer(out_file)
    row0 = next(x)
    row0.append('longitude')
    row0.append('latitude')
    row0.append('geonameId')
#    print(row0)
    for row in x:
      name = row[2]
      city = row[6]
      #state = row[7]
      country = row[8]
      location = city +" "+ country
#      print(location)
      payload = { 'q' : location, 'maxRows' : 1, 'username' : "joshuadull"}
      r = requests.get("http://api.geonames.org/searchJSON", params = payload)
#      print(r.url)
      data = json.loads(r.text)
      try:
        row.append(data['geonames'][0]['lng'])
        row.append(data['geonames'][0]['lat'])
        row.append(data['geonames'][0]['geonameId'])
        w.writerow(row)
#        print(row)
      except:
#        w.write(row)
        print(row)
# http://api.geonames.org/searchJSON?q=warsaw%20poland&maxRows=1&username=joshuadull

with open("deathGeo.csv", "r") as in_file, open("deathGeonames.csv", "w") as out_file:
    x = csv.reader(in_file)
    w = csv.writer(out_file)
    row0 = next(x)
    row0.append('longitude')
    row0.append('latitude')
    row0.append('geonameId')
 #   print(row0)
    for row in x:
      name = row[3]
      city = row[6]
      #state = row[7]
      country = row[8]
      location = city +" "+ country
 #     print(location)
      payload = { 'q' : location, 'maxRows' : 1, 'username' : "joshuadull"}
      r = requests.get("http://api.geonames.org/searchJSON", params = payload)
 #     print(r.url)
      data = json.loads(r.text)
      try:
        row.append(data['geonames'][0]['lng'])
        row.append(data['geonames'][0]['lat'])
        row.append(data['geonames'][0]['geonameId'])
        w.writerow(row)
 #       print(row)
      except:
 #       w.write(row)
        print(row)
