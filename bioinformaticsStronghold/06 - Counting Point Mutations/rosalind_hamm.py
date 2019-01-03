#Given two strings of equal length
#Find the Hamming Distance dH (s,t)
#Outputs solution as a text file: result.txt

#Parse the data from a txt file and return an array with two strings for each sequence
def parseData(fileName):
    file = open(fileName, 'r')
    data = file.read()
    data = data.splitlines()
    file.close()

    return data

#Count the number of differences in each spot between the two sequences
def countPointMutations(data):

    #Split the sequences into different variables
    s = data[0]
    t = data[1]

    #Loop will run through each base of each sequence and add a count if there is a difference between the sequences at each point
    hammingDistance = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            hammingDistance += 1

    #Returns output as a string
    return str(hammingDistance)

#Write the data into an output file
def writeData(fileName, result):
    file = open(fileName, 'w')
    file.write(result)
    file.close()

#Run the entire program
def runProgram():
    #Parse
    data = parseData('rosalind_hamm.txt')
    #Count
    hammingDistance = countPointMutations(data)
    #Write
    writeData('result.txt', hammingDistance)

#Command for running the program
runProgram()
