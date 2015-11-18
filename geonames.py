import requests
import csv

geonames = {}

with open("birth_info.csv", "r") as in_file:
    x = csv.reader(in_file)
    row0 = next(x)
    row0.append('longitude')
    row0.append('latitude')
    print(row0)
    # for row in x:
    #   city = row[6]
    #   state = row[7]
    #   country = row[8]
    #   payload = { 'q' : city +"+"+ state +"+"+ country, 'maxRows' : 1, 'username' : "joshuadull"}
    #   r = requests.get("http://api.geonames.org/searchJSON", params = payload)
    #   print(r)
  # http://api.geonames.org/searchJSON?q=warsaw%20poland&maxRows=1&username=joshuadull


# for artist_name in x:
#     for date in x[artist_name]:
#             try:
#                 dod = int(date + '0101')
#                 end_date = int(date + '1231')
#                 payload = { 'q' : artist_name, 'fq' : "type_of_material.contains:(Obituary)", 'begin_date' : dod, 'end_date' : end_date, 'api-key' : "86e35586ca628b7b5577029c151f825c:17:72915474" } #"section_name.contains:(Obituaries)"
#                 r = requests.get("http://api.nytimes.com/svc/search/v2/articlesearch.json", params = payload)
#                 data = json.loads(r.text)
#                 #print(data['response']['docs'][0]['web_url'])
#                 nyt[artist_name] = [data['response']['docs'][0]['web_url']]
#             except:
#                 continue