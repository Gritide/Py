#Dogukan Celik
#Dogukan.Celik89@myhunter.cuny.edu
#11/13/2019
import folium
import pandas as pd
#cuny = pd.read_csv('de.csv')
#print(cuny["Campus"])
mapCUNY = folium.Map(location=[40.75, -74.125])
newMarker = folium.Marker([40.768731, -73.964915], popup="Hunter College")
newMarker.add_to(mapCUNY)
mapCUNY.save(outfile='nycMap.html')
