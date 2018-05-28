import matplotlib.pyplot as plt
import datetime
import math
import ndbc

# Generates a plot of past month wind speed at a buoy

# Calculates date parameters as previous month
end_time = datetime.datetime.utcnow()
end_time_string = end_time.strftime("%Y-%m-%dT%H:")
# Rounds to the nearest ten minutes
end_time_minute = str(math.floor(float(end_time.minute) / 10.0) * 10).zfill(2)
end_time_string += end_time_minute + "Z"
print(end_time_string)

query = {
    "request" : "GetObservation",
    "service" : "SOS",
    "version" : "1.0.0",
    "offering" : "urn:ioos:station:wmo:44058",
    "observedproperty" : "winds",
    "responseformat" : "text/csv",
    "eventtime" : "latest"
}

api = ndbc.Ndbc(query)

print(api.get_data())
