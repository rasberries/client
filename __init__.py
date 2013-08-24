import requests
import json


url = "http://10.0.0.238:56653/api/values";
r = requests.get(url)
print r.json()
