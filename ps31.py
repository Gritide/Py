
#Dogukan Celik
#Dogukan.Celik89@myhunter.cuny.edu
import pandas as pd
import matplotlib.pyplot as plt
dod=input("Enter name of input file:")
ded=input("Enter name of output file:")
homeless = pd.read_csv(dod)
homeless['Fraction Children']=homeless['Total Children in Shelter']/homeless['Total Individuals in Shelter']
homeless.plot(x = 'Date of Census', y = 'Fraction Children')


plt.savefig(ded)
plt.show()
