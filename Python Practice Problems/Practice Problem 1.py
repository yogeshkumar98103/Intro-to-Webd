# ================================
#        Practice Problem 1
# ================================

n = int(input("Enter n : "))

t1 = 0
t2 = 1

while n>0 :
    t3 = t1 + t2

    print(t1)

    t1 = t2
    t2 = t3
    n-=1