#Dogukan Celik
#Dogukan.Celik89@myhunter.cuny.edu
dod=('If it VERB like a NOUN and LEL like a NOUN, it probably is a NOUN.')

noun=input("Enter a noun: ")
dod=dod.replace('NOUN', noun)
verb=input("Enter a verb: ")
dod=dod.replace('VERB', verb)
verb2=input("Enter another verb: ")
dod=dod.replace('LEL', verb2)

print(dod)

