import geoip2.database
import requests
import json

res = requests.get('https://www.google.com')
data = res.json()
print(data)

reader = geoip2.database.Reader("GeoLite2-City.mmdb")


response = reader.city('90.155.130.10')

print(response)

reader.close()
