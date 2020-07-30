#Dogukan Celik
#Dogukan.Celik89@myhunter.cuny.edu
import numpy as np
import matplotlib.pyplot as plt


#Read in the data to an array, called elevations:
dod=input("How blue is the ocean: ")
ded=input("What is the output file:")
elevations = np.loadtxt('elevationsNYC.txt')

#Take the shape (dimensions) of the elevations
#  and add another dimension to hold the 3 color channels:
mapShape = elevations.shape + (3,)

#Create a blank image that's all zeros:
floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row,col] <= 0:
            #Below sea level
           floodMap[row,col,2] = dod  #Set the blue channel to 100%
        elif elevations[row,col]%10==0:
           floodMap[row,col,0] = 0    #Set the red channel to 100%
        else:
            #Above the 6 foot storm surge and didn't flood
            floodMap[row,col] = 1.0  #Set the green channel to 100%

plt.imshow(floodMap)

#Display the plot:
plt.show()
plt.imsave(ded, floodMap)




