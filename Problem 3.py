# ================================
#             Problem 3
# ================================

inputString = input()
inputString += " "
newData = ""
previous = inputString[0]
times = 1
for i in inputString[1:]:
    if i == previous:
        times+=1
    else:
        newData+=f"({times}, {previous}) "
        times = 1
        previous = i
print(newData)