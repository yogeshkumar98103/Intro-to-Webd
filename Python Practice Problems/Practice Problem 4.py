# ================================
#        Practice Problem 4
# ================================

num = input("Enter a number : ")

def refactor(num):
    if(len(num) <= 3):
        return num
    num = num[:-3] + "," + num[-3:]
    return refactor(num[:-4]) + num[-4:]

formatted_num = refactor(num)
print(formatted_num)
