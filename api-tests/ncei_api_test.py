import requests
import json

# Docs available at https://www.ncdc.noaa.gov/cdo-web/webservices/v2

# You don't get to see my API key
def get_ncei_api_key():
    with open('../.api_keys.json') as f:
        return json.load(f)['NCEI']

header = {'token' : get_ncei_api_key()}
url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data'
query = {
    # Required
    "datasetid" : "GHCND",
    "startdate" : "2018-05-15",
    "enddate" : "2018-05-25",

    # Optional
    "datatypeid" : "TMAX",
    "locationid" : "FIPS:51085",
    "units" : "standard",
    "includemetadata" : "false"
}

data = requests.get(url=url, headers=header, params=query)

print(data.text)
