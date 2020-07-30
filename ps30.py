#Dogukan Celik
#Dogukan.Celik89@myhunter.cuny.edu
import pandas as pd
recipe=input("Enter Name: ")
dod=pd.read_csv(recipe)
dud=lambda x: x*2
dod["Amount"]=dod["Amount"].apply(dud)
print("Double your recipe is= ")
print(dod)


