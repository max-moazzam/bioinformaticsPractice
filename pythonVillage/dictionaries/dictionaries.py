#Problem: Given a string s of length at most 10000 letters
#Return: The number of occurences of each word in s, where words are separated by spaces

#Open the file and get the string
file = open('rosalind_ini6.txt', 'r')

s = file.read()

file.close()

#Break up the string into individual words
s = s.split()

#Count the words
#Create a dictionary to store words
words = {}

#Iterate through the array, check to see if the word is there, if not add it, if it is then add 1 to the value
#Note: Words are case sensitive, so 'This' will be a different word from 'this'
for word in s:
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

#Output dictionary to a text file
output = open('dictionariesOutput.txt', 'w')

for word, amount in words.items():
    outputString = word + ' ' + str(amount)
    output.write(outputString + '\n')

output.close()
