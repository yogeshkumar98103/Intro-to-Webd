# ================================
#             Problem 2
# ================================
from collections import OrderedDict

shoppingList = OrderedDict()

times = int(input())

for _ in range(times):
    splitedData = input().split()
    item = " ".join(splitedData[:-1])
    price = int(splitedData[-1])

    if (shoppingList.get(item) == None):
        shoppingList[item] = price
    else:
        shoppingList[item] += price

for item in shoppingList:
    print(item, shoppingList[item])
