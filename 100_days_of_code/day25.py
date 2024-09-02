def anyDice(sides):
    import random

    result = random.randint(1, sides)
    return result


def dice6_8():
    six = anyDice(6)
    eight = anyDice(8)

    result = six * eight
    return result


print("Character Health Stats")
print()
character = "yes"

while character == "yes":
    health = dice6_8()
    print(f"Character health stat is {health} hp")
    character = input("Generate for another character?: ")
