"""
The module asks the user how they are fairing on.
"""

print()
print("30 Days Down".center(35))
print("....................................")

for i in range(1, 31):
    print()
    answer = input(f"How was Day {i}? : ")
    print()
    print(f"You thought Day {i} was {answer}".center(35))
