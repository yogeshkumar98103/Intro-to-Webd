# ================================
#             Problem 1
# ================================

def is_leap(year):
    leap = False
    if (year % 4 == 0):
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True

        else:
            leap = True
    return leap

# Sample input
# year = int(input("Enter a year : "))
# print(is_leap(year))
