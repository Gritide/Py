#Dogukan Celik
#Dogukan.Celik89@myhunter.cuny.edu
import numpy as np
logoImg = np.ones((30,30,3)) 
logoImg[:,:3,1] = 0 
logoImg[:,-3:,1] = 0 
logoImg[:,:3,:,1] = 0 
plt.imsave("logo.png", logoImg) 
