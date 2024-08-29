print("List Generator!!!!!")
print()
print("We print a list of numbers")
print("Tell us from which number to start and end at")
print()
start = int(input("Start at: "))
end = int(input("End before: "))
increment = int(input("Increment between values: "))
print()

for i in range(start , end, increment):
  print(i)
