import matplotlib.pyplot as plt
import datetime
import math

# Search whole project
import sys
sys.path.append("../")

from api import ndbc

# Generates a plot of past month wind speed at a buoy

# Calculates date parameters as previous 30 days
end_time = datetime.datetime.utcnow()
start_time = end_time - datetime.timedelta(days=30)

# Generates the query and gets the data from the API
query = {
    "request" : "GetObservation",
    "service" : "SOS",
    "version" : "1.0.0",
    "offering" : "urn:ioos:station:wmo:44058",
    "observedproperty" : "winds",
    "responseformat" : "text/csv",
    "eventtime" : ndbc.Ndbc.format_time_range(start_time, end_time)
}
api = ndbc.Ndbc(query)
data = api.get_data()

# Generates the list of wind speeds
graph_data = [float(entry['wind_speed (m/s)']) for entry in data]
date_data = [ndbc.Ndbc.deformat_time(entry['date_time']) for entry in data]

plt.plot(date_data, graph_data)
plt.xlabel("Time")
plt.ylabel("Wind Speed (m/s)")

plt.show()
