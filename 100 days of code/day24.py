def rollDice(sides):
    import random

    roll = random.randint(1, sides)
    print(f"You rolled {roll}")


print("Infinity Dice")
print()
print()
sides = int(input("How many sides?: "))
while True:
    rollDice(sides)
    answer = input("Roll again?: ").lower()

    if answer == "yes":
        continue
    else:
        break
print("Goodbye!")
