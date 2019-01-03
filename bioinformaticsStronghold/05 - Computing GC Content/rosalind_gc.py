#Parses sequence data and ID from text file into an object
def parseSeqData(nameOfDatabase):
    
    #Open the database
    file = open(nameOfDatabase, 'r')

    #Set variables
    firstRun = True #Indicates this is the first run through the following loop

    #Where each sequence tag and sequence will be stored
    allTags = []
    allSeqs = []

    #Temporary variable to store each line of the current sequence
    currentSeq = []

    #Loop will go through each line of the database and organize data into the correct variables
    while True:
        #Loops through each line of the database, with the new line character stripped
        currentLine = file.readline().strip()

        #Last line will be a blank space, will end the loop and append the current sequence to the allSeqs array
        if currentLine == '':
            allSeqs.append("".join(currentSeq))
            break

        #Tags will begin with a '>'
        #If current line is a tag and is the first run, it will be appended to the allSeqs array
        #firstRun will be switched to False to indicate it is no longer the first loop
        elif currentLine[0] == '>' and firstRun == True:
            allTags.append(currentLine)
            firstRun = False
        #If the current line is not a tag each line will be appended to 
        elif currentLine[0] != '>':
            currentSeq.append(currentLine)
        elif currentLine[0] == '>' and firstRun == False:
            allSeqs.append("".join(currentSeq))
            currentSeq = []
            allTags.append(currentLine)

    #Close the file
    file.close()
    #Put it all in an object for easier access
    allData = {
       "tags": allTags,
       "sequences": allSeqs
       }

    return allData

#Takes in an object containing DNA sequences and tags, and prints the largest GC% and its tag
def findGC(data):

    #Set variables
    index = -1 #Starts at -1 because first index will be 0
    highestPercent = 0
    indexOfHighest = 0

    #Go through each sequence, add up G and C, find highest GC percent and the index of that sequence
    for sequence in data["sequences"]:
        index += 1

        count = 0
        totalBases = len(sequence)
        #Iterate through each base in the sequence to find the count of 'G' and 'C'
        for base in sequence:
            if base == 'G' or base == 'C':
                count += 1
        #Find GC percentage
        gcPercent = (count/totalBases) * 100
        #Put highest GC percentage and its index to access later
        if gcPercent > highestPercent:
            highestPercent = gcPercent
            indexOfHighest = index

    #Print the tag of the highest GC content (with starting '>' character removed) and highest GC percent
    print(data["tags"][indexOfHighest][1:] + '\n' + str(highestPercent))

data = parseSeqData('rosalind_gc.txt')
findGC(data)
