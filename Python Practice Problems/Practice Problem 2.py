# ================================
#        Practice Problem 2
# ================================

string = input("Enter a string : ")

short = [x[0] for x in string.split()]
abbrevation = "".join(short)

print(abbrevation)