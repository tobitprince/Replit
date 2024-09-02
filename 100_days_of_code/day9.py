"""
This module says the generation you were born in.
"""

def determine_generation(year_of_birth):
    """
    Determine the generation based on the year of birth.
    """
    if 1925 <= year_of_birth <= 1946:
        return "You are a Traditionalist."
    elif 1947 <= year_of_birth <= 1964:
        return "You are a Baby Boomer."
    elif 1965 <= year_of_birth <= 1981:
        return "You are a Generation X"
    elif 1982 <= year_of_birth <= 1995:
        return "You are a Millenial"
    elif 1996 <= year_of_birth <= 2015:
        return "You are a Generation Z"
    else:
        return "You are a Generation Alpha"

print()
year_of_birth1 = int(input("What year were you born? "))
GENERATION_MESSAGE = determine_generation(year_of_birth1)
print(GENERATION_MESSAGE)