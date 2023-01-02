import requests
import json

base_url = "https://anapioficeandfire.com/api/houses/1"
try:

    r = requests.get(base_url, timeout = 10)
except requests.exceptions.ConnectionError:
      print("invalid URL")
      exit(1)

if(r.status_code != 200):
    print("invalid")
    exit(1)

response = r.json()

# json display
print("Name: ", response.get("name"))        
print("Region: ", response.get("region"))
print("Coat of Arms: ", response.get("coatOfArms"))