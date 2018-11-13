#Problem: Given a file of 1000 lines
#Return: A file of the even numbered lines


#First open the file to extract from, r for read mode
file = open('rosalind_ini5.txt', 'r')

#Puts all the lines in the file into a list
linesInFile = file.readlines()

#Create a linesToWrite list to store the lines that need to be written
linesToWrite = []
#For loop to go through each line
i = len(linesInFile)
for line in range(i-1):
    #Looking for even lines, but we're starting at 1 not 0, so actually looking for odd lines
    if line % 2 != 0:
        #Create a list of even numbered lines
        linesToWrite.append(linesInFile[line])

#Close the current file open
file.close()

#Create a new file, w for write mode
file = open('newFile.txt', 'w')

#For loop to go through each line in the linesToWrite list, adds a space after each
for line in linesToWrite:
    file.write(line)

#Close the current file
file.close()
        
