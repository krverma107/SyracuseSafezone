## What we are trying to create:

Our team’s plan is to create an application using Syracuse’s Open Data API to generate an interactive map that displays the crimes and fires in the Syracuse area. 

## Inspiration
Our inspiration was to create a project that helps anyone looking to buy a property in the Syracuse area find the safest areas to live.

## What it does
It uses the Syracuse OpenData API to get crime rate and police data to generate a map of the Syracuse area with the past criminal offenses and fire incidents as blue and red dots respectively.

## How we built it
We built it using the Syracuse OpenData API and integrated that into our python code. We used python libraries like folium, json, pandas, requests.API to generate our maps and create the json files to work with data in a tabular form. We then used the address attribute from the data and converted it into tuples of (latitude, longitude) values using Nominatim from the python geopy library. 

## Challenges we ran into

We needed to plot the coordinates on the map. So at first, we had issues with using the geopy library effectively to convert our physical addresses into (latitude, longitude) coordinate points. We faced a problem when the code returned an attribute error of Nonetype for some of the addresses as they did not exist on the map. We fixed that by including the try-except syntax structure into our code.

## Accomplishments that we're proud of
We are proud of being able to use the OpenData API effectively, importing the data into our code, and using python libraries we had not heard about before to convert our addresses into coordinates on a map.

## What we learned

We learned more about python libraries and how they tremendously increase the capabilities that python has to offer. We also learned how to effectively use a third-party website's API and use their data in our code.

## What's next for CuseHacks Project

We have planned on adding more features like:

* Add a user-input feature where the user is able to input their address and mile radius within which they would like to see crime and fire data.
* Long-term goal: to add more data such as natural calamities in the area, weather hazards, water quality, access to hospitals, and educational institutions. 
* We also plan to expand beyond the Syracuse area by letting users enter their zip codes and accessing relevant data for the given mile radius.

