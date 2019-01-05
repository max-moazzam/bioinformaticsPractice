#Given a number of Homozygous Dominant (k), Heterozygous (m), and Homozygous Recessive individuals
#Return the probability that a randomly selected pair will have an offspring with at least one dominant allele

#Parse Data
def parse(filename):
    file = open(filename, 'r')
    data = file.read().split()
    file.close()

    return data
    
#Find probability
def findProbability(data):

    #Homozygous Dominant (AA)
    k = int(data[0])
    #Heterozygous (Aa)
    m = int(data[1])
    #Homozygous Recessive (aa)
    n = int(data[2])

    total = k + m + n


    #Probability k will be selected as mate 1 will be k/total
    #For mate 2 we know there is 1 less in the total and k is 1 less
    #Homozygous dominant paired with any combination will result in at least 1 dominant allele offspring
    kFirst = (k/total) * (((k-1)/(total-1)) + (m/(total-1)) + (n/(total-1)))

    #Heterozygous + Heterozygous = 75% chance of dominant allele passed, Heterozygous + Homozygous Recessive = 50% chance
    mFirst = (m/total) * ((k/(total-1)) + (((m-1)/(total-1)) *.75) + ((n/(total-1))*.5))

    #Homozygous Recessive + Heterozygous = 50% chance of dominant allele passed, Homozygous Recessive + Homozygous Recessive = 0% chance
    nFirst = (n/total) * ((k/(total-1)) + ((m/(total-1))*.5) + (((n-1)/(total-1))*0))

    probability = kFirst + mFirst + nFirst

    return str(probability)

#Write Data
def writeData(result):
    file = open('result.txt', 'w')
    file.write(result)
    file.close()

#Run Function
def runFunction():
    data = parse('rosalind_iprb.txt')
    result = findProbability(data)
    writeData(result)

runFunction()

