import requests
import json

url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/locations.json"

response = requests.get(url)
print(response.text) # This one shows the html 
print(response.content) # Displays in json format
json_content = json.loads(response.text) 
# json.loads(response.content) This one is less organised but still looks organized
print(json.dumps(json_content, indent=4)) #Displays in a more organised format
