#Rabbits and Recurrence Relations
#Given:  Positive integers n≤40 and k≤5
#Return: The total number of rabbit pairs that will be present after n months,
#       if we begin with 1 pair and in each generation, every pair of reproduction-age
#       rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

#Open input and extract data
file = open('rosalind_fib.txt', 'r')
numberString = file.read()
numberString = numberString.split()
file.close()
numberInt = []

for number in numberString:
    numberInt.append(int(number))

#Start with a base case
#Use recursion
#Since the number of offspring is the same as the amount alive two months prior...
#...we can say that the number of pairs is the number of pairs in the previous month...
#...+ the number of pairs in the previous months multiplied by the amount of offspring

def rabbitCounter(n,k):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return rabbitCounter(n-1,k) + k*rabbitCounter(n-2,k)

#Output
result = rabbitCounter(*numberInt)
output = open('fibOutput.txt', 'w')
output.write(str(result))
output.close()


