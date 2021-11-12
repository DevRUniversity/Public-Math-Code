# Code made by Devon R,

import sympy
import numpy
import matplotlib.pyplot as p1
import matplotlib.markers as MARKERS

ListOfSums = []
limitOfPrimeNumbers = int(input("Type a integer limit value for how many prime numbers you want to check up too:"))
GapsRequested = input("Type a integer limit value for how many Gap Iterations you want to check up too, or type \"All\" if you want to see all:")
if(GapsRequested == "All"):
    limitOfPrimeGapIterations = -1
else:
    limitOfPrimeGapIterations = int(GapsRequested)
listOfPrimes = []
IteratedPrimeGaps = []

def GenerateGaps(var):
    ReturnedOutputListOfGaps = []

    for i in range(1,len(var)):
        ReturnedOutputListOfGaps.append(var[i]-var[i-1])

    return ReturnedOutputListOfGaps

for i in range(1,limitOfPrimeNumbers):
    if(sympy.isprime(i)):
        listOfPrimes.append(i)

IteratedPrimeGaps.append(listOfPrimes)
if(limitOfPrimeGapIterations == -1):
    limitOfPrimeGapIterations = len(listOfPrimes)
GapIndex = 0



while(GapIndex < limitOfPrimeGapIterations):

    IteratedPrimeGaps.append(GenerateGaps(IteratedPrimeGaps[GapIndex]))
    GapIndex = GapIndex + 1

for i in range(len(IteratedPrimeGaps)):
    print("Number of Items in Difference Set: " + str(len(IteratedPrimeGaps[i])), "Difference Set:" + str(IteratedPrimeGaps[i]))
    if (len(IteratedPrimeGaps[i]) == 0):
        print("Remaining Difference Sets have zero elements")
        break

StatusRequestSumOfSets = input("Do you want to see the sum of the elements for these Difference sets? [Y/N]")
if(StatusRequestSumOfSets != "Y" and StatusRequestSumOfSets != "y"):
    print("User did not request to see the sum of Differences of sets, closing program!")
    exit(0)
else:

    print("\n \n \n \n \nSum of Each Set Difference shown below...")
    for i in range(0,len(IteratedPrimeGaps)):
        sum = 0
        for j in range(0,len(IteratedPrimeGaps[i])):
            sum = IteratedPrimeGaps[i][j] + sum
        print("Sum of Each Difference Set with size " + str(len(IteratedPrimeGaps[i])) + " = ", sum)
        ListOfSums.append(sum)
        sum = 0

XListOFSums = []
for i in range(0,len(ListOfSums)):
    XListOFSums.append(i)

p1.plot(XListOFSums, ListOfSums, color = "red")
p1.xlabel("Iteration from Prime Numbers")
p1.ylabel("Sum of each Set")
p1.title("nth Prime Gaps")
p1.show()