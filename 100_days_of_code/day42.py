"""
something something
"""
import os

def new_print(data_type):
    """_summary_

    Args:
        data_type (_type_): _description_
    """
    if data_type == "Earth":
        print("\033[32m", end="")
    elif data_type == "Air":
        print("\033[37m", end="")
    elif data_type == "Fire":
        print("\033[31m", end="")
    elif data_type == "Water":
        print("\033[34m", end="")
    else:
        print("\033[0m", end="")

thismokebeast = {"Beast Name": None, "type":None,
                 "Special Move": None,"Starting HP":"",
                 "Starting MP":None}
os.system("cls")
print("MokeBeast-Generic Beast Battle Game".center(70,"-"))
for moke in thismokebeast:
    thismokebeast[moke] = input(f"Input your {moke}: ").strip().title()

print()

new_print(thismokebeast['type'])
print(f"Your beast is called {thismokebeast['Beast Name']}."
      f"It is a {thismokebeast['type']} beast with a " 
      f"special move of {thismokebeast['Special Move']}")
new_print("end")
