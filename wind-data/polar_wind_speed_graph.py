import matplotlib.pyplot as plt
import matplotlib
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
speed_data = [float(entry['wind_speed (m/s)']) for entry in data]

def generate_direction(direction):
    return float(direction) if direction != "" else -1.0

direction_data = [generate_direction(entry['wind_from_direction (degree)']) for entry in data]

length = len(direction_data)
for i in range(0, ):
    if direction_data[i] == -1.0:
        del(direction_data[i])
        del(speed_data[i])
        length -= 1

direction_data = [math.radians(entry) for entry in direction_data]

# Data
figure = plt.figure()
ax = figure.gca(projection="polar")
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
ax.plot(direction_data, speed_data, "bo")

plt.show()
