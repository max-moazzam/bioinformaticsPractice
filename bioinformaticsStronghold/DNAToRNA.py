#Input a string
file = open('rosalind_rna.txt', 'r')
s = file.read()
file.close()

#Split the string into a list
s = list(s)

#Iterate through the list
#Check to see if it's a U, if it is switch to a T
i = len(s) - 1
for letter in range(i):
    if s[letter] == 'T':
        s[letter] = 'U'

#Join the string
s = ''.join(s)

#Output
output = open('DNAToRNA_output.txt', 'w')
output.write(s)
output.close()


