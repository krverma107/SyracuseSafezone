from requests.api import head
import pandas as pd
import requests
import json
import folium
from geopy.geocoders import Nominatim
data_source = "https://services6.arcgis.com/bdPqSfflsdgFRVVM/arcgis/rest/services/WeeklyOffensesII_CityHall/FeatureServer/0/query?where=1%3D1&outFields=DATEEND,DRNUMB,ADDRESS,CODE_DEFINED&outSR=4326&f=json"
response1 = requests.get(data_source)
data1 = response1.json()
data1 = pd.json_normalize(data1['features'],errors='ignore')

data1.rename(columns={
    'attributes.ADDRESS': 'Address'}, inplace=True)

for index, row in data1.iterrows():
  data1.loc[index,'Address'] = str.rstrip(data1.loc[index,'Address']) + " Syracuse"

#adds lat and long coordinates to the dataset
for index1, row in data1.iterrows():
  tempstring = data1.loc[index1,'Address']
  tempstring = str(tempstring)
  try:
    geolocator1 = Nominatim(user_agent="Untitled"+str(index1)+".ipynb")
    location1 = geolocator1.geocode(tempstring, timeout = 2)
    data1.loc[index1,'X'] = location1.latitude
    data1.loc[index1,'Y'] = location1.longitude
  except AttributeError:
    data1.loc[index1,'X'] = 0
    data1[index1,'Y'] = 0
data1.to_pickle("crimedata.pkl")