#Dogukan Celik
#Dogukan.Celik89@myhunter.cuny.edu
import folium
import pandas as pd
import math
ded=input("Enter a file name:")
dod=input("Enter output file name:")
cuny=pd.read_csv(ded)

#Create a map, centered (0,0), and zoomed out a bit:
mapWorld = folium.Map(location=[0, 0],zoom_start=3)
for index, row in cuny.iterrows():
    lat=row["LATITUDE"]
    lon=row["LONGITUDE"]
    time=row["TIME"]
    print(time)
    if(math.isnan(float(lat)) or math.isnan(float(lon))):
        pass
    else:
        newMarker = folium.Marker([lat,lon], popup=time)
        newMarker.add_to(mapWorld)
#Save the map:
mapWorld.save(outfile=dod)
