"""
A factorial is the product of all the numbers up to a value, starting from 1.
For example, factorial 5 would be 1 * 2 * 3 * 4 * 5 = 120
1. Write a function that:
1. Starts at the highest number.
2. Multiplies that by factorial of itself minus one
3. Terminates when it reaches 1 and returns 1
4. Outputs the factorial.
"""

import os
import time

def factorial(value):
    """_summary_

    Args:
        value (_type_): _description_

    Returns:
        _type_: _description_
    """
    if value == 1:
        return 1
    return value * factorial(value-1)
def main():
    """_summary_
    """
    os.system("cls")
    print("Factorial Finder".center(40, "*"))
    number = int(input("Input a number: "))
    for i in range(1, 10):
        print("Computing"+ "."*i)
        time.sleep(0.3)
        os.system("cls")
    answer = factorial(number)
    print(f"The factorial of {number} is {answer}")

if __name__ == "__main__":
    while True:
        main()
        time.sleep(2)
