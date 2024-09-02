print("Math Game!!!!!!!")
print()
print("We're going to test your multiplication knowledge")
print()
multiple = int(input("Name your multiples: "))
point = 0
for i in range(1, 11):
    answer = int(input(f"What is {i} *  {multiple} = ?: "))
    if answer == i * multiple:
        print("That's amazing")
        point += 1
    else:
        print(f"That is not correct , The answer was {i*multiple}")
if point == 10:
    print()
    print("Amazing you got everything :)))")
else:
    print()
    print(f"You scored {point} out of 10")
