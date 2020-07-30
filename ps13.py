#Dogukan Celik
#Dogukan.Celik89@myhunter.cuny.edu
import matplotlib.pyplot as plt
import numpy as np

ded=input("Enter name of the input file:")
img = plt.imread(ded)   
plt.imshow(img)		           
plt.show()                         

img2 = img.copy()        
img2[:,:,1] = 0
img2[:,:,2] = 0          

plt.imshow(img2)         
plt.show()               

plt.imsave('reds.png', img2)  
