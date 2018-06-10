import requests
import json
import math
import datetime

# Adapted from ndbc_sos_api_test.py to easily get data from NDBC API
class Ndbc:

    # The URL at which the NDBC API is located
    url = 'https://sdf.ndbc.noaa.gov/sos/server.php/get'

    # Stores the results for a query in a new Ndbc object.
    # See the documentation at
    # https://sdf.ndbc.noaa.gov/sos/
    # for proper formatting.
    def __init__(self, query):
        r = requests.get(self.url, params=query)

        if r.status_code == requests.codes.ok:
            self._raw_data = r.text
        else:
            print("Connection error, status code " + r.status_code)

    # Gets a Python list of each requested entry.
    # Each entry is a Python dictionary.
    def get_data(self):
        entries = self._raw_data.splitlines()
        fieldnames = entries[:1][0].split(',')

        fieldnames = [field[1:-1] if field.startswith('"') and field.endswith('"')
            else field for field in fieldnames]

        data_pydict = []
        for entry in entries[1:]:
            fieldnames_iterator = iter(fieldnames)
            entry_dict = {}

            for data_point in entry.split(','):
                entry_dict[next(fieldnames_iterator)] = data_point

            data_pydict.append(entry_dict)
        return data_pydict

    # Gets a JSON file of the requested data
    def get_data_json(self):
        return json.dumps(get_data())

    # Floors to the nearest ten, returns string with 2 digits
    @staticmethod
    def _round_to_ten(x):
        return str(math.floor(float(x) / 10.0) * 10).zfill(2)

    # Formats a datetime object to match API
    @staticmethod
    def format_time(datetime_obj):
        return datetime_obj.strftime("%Y-%m-%dT%H:") + Ndbc._round_to_ten(datetime_obj.minute) + "Z"

    # Formats a datetime range to match API
    @staticmethod
    def format_time_range(start_time, end_time):
        return Ndbc.format_time(start_time) + "/" + Ndbc.format_time(end_time)

    # Converts API datetime back to Python datetime
    @staticmethod
    def deformat_time(api_time):
        return datetime.datetime(year=int(api_time[0:4]), month=int(api_time[5:7]),
            day=int(api_time[8:10]), hour=int(api_time[11:13]), minute=int(api_time[14:16]))
