from requests.api import head
import pandas as pd
import requests
import json
import folium
data_source = "https://services6.arcgis.com/bdPqSfflsdgFRVVM/arcgis/rest/services/Fire_Incidents/FeatureServer/0/query?where=1%3D1&outFields=propertyuse,compositeaddress,postalcode,X,Y,incidenttype,incidentnumber,alarmdate&outSR=4326&f=json"
response = requests.get(data_source)
response.status_code
fire_data = response.json()
fire_data = pd.json_normalize(fire_data['features'],errors='ignore')

fire_data.rename(columns={
    'attributes.compositeaddress': 'Address',
    'attributes.postalcode': 'ZIP code',
    'attributes.X': 'X',
    'attributes.Y': 'Y'}, inplace=True)

crime_data1 = pd.read_pickle("crimedata1.pkl")
crime_data2 = pd.read_pickle("crimedata2.pkl")

map = folium.Map(location=[43.0493, -76.1455], zoom_start=12)
#fire points
for index, row in fire_data.iterrows():
  folium.CircleMarker([row['Y'], row['X']], radius=3, fill = True, color='red', fill_color = 'red', popup='Address: ' + str(row['Address'])).add_to(map)
#crime1 points
for index, row in crime_data1.iterrows():
  if crime_data1.loc[index,'X'] == 0:
    continue
  folium.CircleMarker([row['X'], row['Y']], radius=3, fill = True, color='blue',fill_color = 'blue', popup='Address: ' + str(row['Address'])).add_to(map)
#crime2 points
for index, row in crime_data2.iterrows():
  if crime_data2.loc[index,'X'] == 0:
    continue
  folium.CircleMarker([row['X'], row['Y']], radius=3, fill = True, color='blue', fill_color = 'blue',  popup='Address: ' + str(row['Address'])).add_to(map)
map