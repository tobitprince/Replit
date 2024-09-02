"""
    This module calculates the grade.
"""

testName = input("What is the name of the test? ")
maxScore = int(input("What is the maximum score? "))
score = int(input("What is your score? "))

percentage = round(float(score / maxScore) * 100, 2)

if percentage < 50:
    print("Your percentage is ", percentage, ",Grade is U")
elif percentage < 60:
    print("Your percentage is ", percentage, ",Grade is D")
elif percentage < 70:
    print("Your percentage is ", percentage, ",Grade is C")
elif percentage < 80:
    print("Your percentage is ", percentage, ",Grade is B")
elif percentage < 90:
    print("Your percentage is ", percentage, ",Grade is A")
else:
    print("Your percentage is ", percentage, ",Grade is A+")
