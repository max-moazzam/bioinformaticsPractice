#Given: A DNA string s of length at most 1000 nt.
#Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s

#Open the file, extract the string
file = open('rosalind_dna.txt', 'r')

s = file.read().strip()

file.close()

#Separate the letters in the string, iterate through, and put in a dictionary
#Separate the letters
s = list(s)

#Declare the dictionary
bases = {}

#Iterate through, check to see if a base is already in the dict, if not add, if so add +1 to the value
for base in s:
    if base in bases:
        bases[base] += 1
    else:
        bases[base] = 1

#Print Out (separated by space, in order A,C,G,T)
orderedBases = [bases['A'], bases['C'], bases['G'], bases['T']]

print(' '.join(str(base) for base in orderedBases))
