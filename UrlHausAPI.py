import requests
import json
import csv

url = 'https://urlhaus.abuse.ch/downloads/csv_recent'

response = requests.get(url, stream= True)
response.raise_for_status()

with open('data.csv', 'wb') as fd:
    for chunk in response.iter_content(chunk_size=50000):
        print('Received a chunk')
        fd.write(chunk)

