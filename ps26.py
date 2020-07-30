#Dogukan Celik
#Dogukan.Celik89@myhunter.cuny.edu
import matplotlib.pyplot as plt
import pandas as pd


dood=input("Enter output file name:")
ded=input("What is the output file:")
pop = pd.read_csv('nycHistPop.csv',skiprows=5)

pop['Fraction'] = pop[dood]/pop['Total']

pop.plot(x = 'Year', y = 'Fraction')

fig = plt.gcf()
plt.show()
plt.imshow()
fig.savefig(ded)
