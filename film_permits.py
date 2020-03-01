#Dogukan Celik
#Dogukan.Celik89@myhunter.cuny.edu
import pandas as pd
dod=input("Enter a file name= ")
home=pd.read_csv(dod)
permits=(home['Borough'].value_counts()[0]+home['Borough'].value_counts()[1]+home['Borough'].value_counts()[2]+home['Borough'].value_counts()[3]+home['Borough'].value_counts()[4])
print("There were", permits, "film permits")
print(home['Borough'].value_counts())
print("The five most popular filming locations were: ")
ded=home['ParkingHeld'].value_counts()
print(ded)
