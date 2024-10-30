"""
You're going to write a program that checks a string to see if it is a palindrome.
Yes. We know that Python has the built in function string.reverse() that you could use.
Zero points for that today, we want you to think hard and utilize your skills in:
recursion
string slicing
looping
Your program should:
1. Prompt the user to input a word.
2. Analyze the word to see if it is a palindrome.
3. Output a relevant 'yes/no message.
"""
import os
import time

def is_palindrome(word):
    """_summary_

    Args:
        word (_type_): _description_

    Returns:
        _type_: _description_
    """
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])

def main():
    """_summary_
    """
    os.system("cls")
    print("Palindrome Checker".center(45, "*"))
    word = input("Input a word: ").lower()
    if is_palindrome(word):
        print(f"{word.title()} is a palindrome")
    else:
        print(f"{word.title()} is not a palindrome")

if __name__ == "__main__":
    while True:
        main()
        time.sleep(1)
