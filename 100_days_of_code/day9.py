"""
    This module says the generation you were born in.
"""

print()
yob = int(input("What year were you born? "))
if yob >= 1925 and yob <= 1946:
    print("You are a Traditionalist.")
elif yob >= 1947 and yob <= 1964:
    print("You are a Baby Boomer.")
elif yob >= 1965 and yob <= 1981:
    print("You are a Generation X")
elif yob >= 1982 and yob <= 1995:
    print("You are a Millenial")
elif yob >= 1996 and yob <= 2015:
    print("You are a Generation Z")
else:
    print("You are a Generation Alpha")
