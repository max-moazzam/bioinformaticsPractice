#Given two positive integers: a and b; Return: Sum of all odd integers from a:b inclusive

#Declare start and end and cariable to hold sum
a = 4039
b = 8057

oddSum = 0

#Run through every number, find if odd, add if odd
for number in range(a, b+1):
    if number % 2 != 0:
        oddSum = number + oddSum

print(oddSum)
