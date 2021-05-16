import requests
import json
Team = input("Enter the team: ")
key = 'f51f01afdbmsh26613cef2ae766dp1a702fjsn408791924ac8'
payload = {'q': team, 'appid': key, 'units': 'metric'}
url = f'https://api-football-v1.p.rapidapi.com/v3/Football', params=payload)
r = requests.get(url)
# payload = {'leaguename':'serie a' 'club name': 'AC Milan'}
# r = requests.get('http://httpbin.org/get', params=payload)
# print(r.text)
payload = {'leaguename':'serie a' 'club name': 'AC Milan'}
r = requests.post('http://httpbin.org/post', data=payload)
print(r.text)

res = json.loads(r.text)


with open('data.json', 'w') as f:
    json.dumps(res, f, indent=4)

print('ფეხბურთელები: ' res['main']['squad']), 'F')
print('შედეგები: ' res['main']['results']), 'G')
