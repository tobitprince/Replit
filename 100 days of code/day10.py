bill = float(input("What was the total bill? KES "))
tip = int(input("What percentage tip would you like? "))
total = bill + (bill*tip/100)
people = int(input("How many people to split the bill? "))
answer = total/people
answer= round(answer, 2)
print("Each person should pay: KES ", answer)
