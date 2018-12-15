# ================================
#        Practice Problem 5
# ================================

def frequency(numList):
    numDict = {}

    for num in numList:
        if(numDict.get(num) == None):
            numDict[num] = 1
        else:
            numDict[num]+=1

    for key in sorted(numDict.keys()):
        print(key,":",numDict[key])

# Sample Test Case
numList = [7, 1, 9, 3, 7, 2, 8, 9, 3,]
frequency(numList)
