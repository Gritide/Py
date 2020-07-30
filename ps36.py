#Dogukan Celik
#Dogukan.Celik89@myhunter.cuny.edu
binString=input("Enter a binary number -> ")
decNum=0
for c in binString:
    decNum=decNum*2
    if c=='1':
        decNum=decNum+1

print("Your number in decimal is ",decNum)
