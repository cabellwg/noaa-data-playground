import requests
import json

# Docs available at https://sdf.ndbc.noaa.gov/sos/

url = 'https://sdf.ndbc.noaa.gov/sos/server.php/get'
query = {
    "request" : "GetObservation",
    "service" : "SOS",
    "version" : "1.0.0",
    "offering" : "urn:ioos:station:wmo:44058",
    "observedproperty" : "winds",
    "responseformat" : "text/csv",
    "eventtime" : "2018-05-26T23:40Z/2018-05-27T00:20Z"
}

raw_data = requests.get(url, params=query).text;

entries = raw_data.splitlines()
fieldnames = entries[:1][0].split(',')

def trim_quotes(string):
    return string[1:-1] if string.startswith('"') and string.endswith('"') else string

fieldnames = [trim_quotes(field) for field in fieldnames]

# The queried data as a Python dictionary
data = []
for entry in entries[1:]:
    fieldnames_iterator = iter(fieldnames)
    entry_dict = {}

    for data_point in entry.split(','):
        entry_dict[next(fieldnames_iterator)] = data_point

    data.append(entry_dict)

# The queried data as json
data_json = json.dumps(data)
print(data_json)
