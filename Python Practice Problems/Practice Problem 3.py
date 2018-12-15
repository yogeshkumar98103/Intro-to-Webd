# ================================
#        Practice Problem 3
# ================================

def findGCD(a,b):
    if b == 0:
        return a
    return findGCD(b,a%b)

a = int(input("Enter first Number : "))
b = int(input("Enter second Number : "))

gcd = findGCD(a,b)
print(gcd)