#Dogukan Celik
#Dogukan.Celik89@myhunter.cuny.edu
dod = input("Please enter your list of names: ").split("; ")
print("\nYou entered:\n")
for i in dod:
    hel = i.split(", ")
    dc = hel[0]
    cd = hel[1]
    print(cd[0]+". "+dc)
print("\nThank you for using my name organizer")
