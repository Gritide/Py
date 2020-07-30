#Dogukan Celik
#Dogukan.Celik89@myhunter.cuny.edu

import pandas as pd
import matplotlib.pyplot as plt
dod=input("Enter name of input file:")
ded=input("Enter name of output file:")
df = pd.read_csv(dod)
df['Date'] = pd.to_datetime(df['Date'].apply(str))
df['% Attending']=100*df['Present']/df['Enrolled']
df.plot(x = 'Date', y = '% Attending')

fig=plt.gcf()
fig.savefig(ded)
