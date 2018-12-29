#Will extract data from a .txt file database and return an object with DNA Tags and Sequences

def numberOfID(nameOfDatabase):

    #Open the file and extract the data
    file = open(nameOfDatabase, 'r')
    allData = file.read()
    file.close()

    #Count how many ID's (all ID's start with '>')
    howManyID = 0
    for letter in allData:
        if letter == ">":
            howManyID += 1

    return howManyID

totalID = numberOfID('rosalind_gc.txt')

#Create an array of objects to store all ID's and Sequences
listOfSeq = []

seqStore = {
    "id": 'notFull',
    "sequence": ''
    }


file = open('rosalind_gc.txt', 'r')

i=0
while True:
    currentLine = file.readline().strip()

    if currentLine == '':
        break
    elif currentLine[0] == '>' and len(listOfSeq) > 0:
        seqStore["sequence"] = "".join(seqStore["sequence"])
        listOfSeq.append(seqStore)
        seqStore = {
            "id": 'notFull',
            "sequence": ''
        }
        seqStore["id"] = currentLine
    elif currentLine[0] == '>' and len(listOfSeq) == 0:
        seqStore["id"] = currentLine
    elif currentLine[0] != '>':
        seqStore["sequence"] = seqStore["sequence"] + currentLine
    
        
    #elif currentLine[0] != '>':
 #       listOfSeq[i]["sequence"].append(currentLine)
 #       listOfSeq[i]["sequence"] = "".join(listOfSeq[i]["sequence"])

#Go through the file line by line, stripping
#If line starts with a > put that in ID
#If line does not start with a >, put that in sequence and strip
#Join all the lines in sequence
#When a new > is found, make it a new position in the array'''
