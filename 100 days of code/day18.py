print("Guess the number")
print()
number = 3
print("I want you to guess the number I am thinking, it's between 1 and 10")
print()
count = 1

while True:
  numero = int(input("What is your guess?: "))
  if numero < number:
    print("Oops that's too low , that's not the number .Try something higher")
    print()
    count += 1
    continue
  elif numero > number:
    print("Oops that's too high , that's not the number .Try something lower")
    print()
    count += 1
    continue
  else:
    print()
    print("Are you charles Xavier? How did you know? :))")
    break
if count ==1 :
  print("And it only took you 1 attempt")
  print()
else:
  print("It took you 3 attempts")
  