import json
import requests
season = input("Enter the year: ")
key = "f51f01afdbmsh26613cef2ae766dp1a702fjsn408791924ac8"
payload = {'x-rapidapi-key' key, 'season': 'number'}
r = requests.get('https://api-football-v1.p.rapidapi.com/v3/standings' params=payload)

res = json.loads(r.text)
print(json.dump(res, indent=4))

# ეს თემა კარგად ვერ გავიგე და გამოვასწორებ აუცულებლად :))