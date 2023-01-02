import requests

#get request
response = requests.get("https://www.anapioficeandfire.com/api/houses/1")

#response parsing
data = response.json()
#print details
print("Name:", data["name"])
print("Region:", data["region"])
print("Coat of Arms:", data["coatOfArms"])