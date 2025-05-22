# Historic daily readings - All Stations
# https://environment.data.gov.uk/flood-monitoring/archive/readings-2025-04-27.csv
import pandas as pd
import requests


root = "https://environment.data.gov.uk/flood-monitoring/archive/readings-"
start = "2025-04-23"
end = "2025-04-24"

def extract(date):
   r = requests.get(f'{root}{date}.csv')
   print(r.text)
   print(type(r))
   return r
extract("2025-0104-01")

# print(r)
# type(r)

# daterange = pd.date_range(start, end)
# for day in daterange:
#     print(day)