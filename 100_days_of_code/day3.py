"""
    This program asks the user for 5 inputs and then prints a menu using those inputs.
"""

typeFood = input("Name a food: ")
typePlant = input("Name a type of plant: ")
typeCooking = input("Name a method of cooking: ")
typeBurned = input("What word describes burned food?: ")
typeItem = input("Name a DIY item: ")

print()
print("MENU")

print("Saute", typeFood, "with", typeBurned, typePlant, "on a bed of", typeItem)