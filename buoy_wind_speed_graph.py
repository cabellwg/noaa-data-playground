import matplotlib.pyplot as plt
import datetime
import math
import ndbc

# Generates a plot of past month wind speed at a buoy

# Floors to the nearest ten, returns string with 2 digits
def round_to_ten(x):
    return str(math.floor(float(x) / 10.0) * 10).zfill(2)

# Formats a datetime object to match API
def format_for_api(datetime_obj):
    return datetime_obj.strftime("%Y-%m-%dT%H:") + round_to_ten(datetime_obj.minute) + "Z"

# Calculates date parameters as previous 30 days
end_time = datetime.datetime.utcnow()
end_time_string = format_for_api(end_time)

start_time = end_time - datetime.timedelta(days=30)
start_time_string = format_for_api(start_time)

# Generates the query and gets the data from the API
query = {
    "request" : "GetObservation",
    "service" : "SOS",
    "version" : "1.0.0",
    "offering" : "urn:ioos:station:wmo:44058",
    "observedproperty" : "winds",
    "responseformat" : "text/csv",
    "eventtime" : start_time_string + "/" + end_time_string
}
api = ndbc.Ndbc(query)
data = api.get_data()

# Generates the list of wind speeds
graph_data = [float(entry['wind_speed (m/s)']) for entry in data]

plt.plot(graph_data)
plt.show()
