#Dogukan Celik
#Dogukan.Celik89@myhunter.cuny.edu
dod=input("Enter a DNA string: ")
d=len(dod)
print("Length is ",d)
numC = dod.count('C')
numG = dod.count('G')	
gc = (numC + numG) / d
print("GC-content is",gc)
