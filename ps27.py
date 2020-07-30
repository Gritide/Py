#Dogukan Celik
#Dogukan.Celik89@myhunter.cuny.edu
import matplotlib.pyplot as plt
import pandas as pd


dood=input("Enter output file name:")
pop = pd.read_csv('nycHistPop.csv',skiprows=5)

pop['Fraction'] = pop[dood]/pop['Total']

print("Maximum population: ",pop[dood].max())
print("Average population: ",pop[dood].mean())
print("Minimum population: ",pop[dood].min())
pop.plot(x = 'Year', y = 'Fraction')

fig = plt.gcf()
fig.savefig("ded.png")
