#Reverse Complement
#Given: A DNA sequence s of 1000bp
#Return: The reverse complement.

#Open file and extract sequence
file = open('rosalind_revc.txt', 'r')
s = file.read()
file.close()

#Reverse the string
reversedS = s[::-1]
#Split the string into an array
sequence = list(reversedS)
#Iterate over the array and create a new array with the complement base
i = len(sequence)
for base in range(i):
    if sequence[base] == 'A':
      sequence[base] = 'T'
    elif sequence[base] == 'T':
        sequence[base] = 'A'
    elif sequence[base] == 'C':
        sequence[base] = 'G'
    elif sequence[base] == 'G':
        sequence[base] = 'C'

finalS = ''.join(sequence)

#Output file
output = open('reverseComplementOut.txt', 'w')
output.write(finalS)
output.close()

