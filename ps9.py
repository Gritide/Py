#Dogukan Celik
#Dogukan.Celik89@myhunter.cuny.edu
word = input("Enter a word: ")
codedWord = ""
for ch in word:
        offset = ord(ch) - ord('a') + 13 
        wrap = offset % 26  
        newChar = chr(ord('a') + wrap)  
        codedWord = codedWord + newChar 
print("Your word in code is: ", codedWord)
