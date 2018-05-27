import requests
import csv

url = 'https://sdf.ndbc.noaa.gov/sos/server.php/get'
query = {
    "request" : "GetObservation",
    "service" : "SOS",
    "version" : "1.0.0",
    "offering" : "urn:ioos:station:wmo:44058",
    "observedproperty" : "waves",
    "responseformat" : "text/csv",
    "eventtime" : "2018-05-26T23:40Z/2018-05-27T00:20Z"
}

data = requests.get(url, params=query).text;

print(data)
