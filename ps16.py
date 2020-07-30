#Dogukan Celik
#Dogukan.Celik89@myhunter.cuny.edu
import math

second=int(input("number of second until lecture starts.: "))
hours=second//3600
print("hours: ", hours)
sec_rem = second % 3600
minutes=sec_rem//60
print("Minutes: ",minutes)
rem_sec=sec_rem%60
print("Seconds: ",rem_sec)
