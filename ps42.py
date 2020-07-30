#Dogukan Celik
#Dogukan.Celik89@myhunter.cuny.edu
import folium
import pandas as pd
ded=input("Enter a file name=")
cuny = pd.read_csv(ded)
print(cuny["Campus"])
mapCUNY = folium.Map(location=[40.768731, -73.964915])
for index,row in cuny.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    name = row["Campus"]
    popup="Hunter College"
    folium.Marker([lat, lon],popup).add_to(mapCUNY)
mapCUNY.save(outfile='City_University_of_New_York__CUNY__University_Campus_Locations_Map.html')
