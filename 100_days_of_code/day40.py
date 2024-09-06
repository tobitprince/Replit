"""
Dictionaries are used to store data values in key:value pairs.
"""

import os
import time

thisdict = {"name":"","dob":"","telephone":"","email":"","address":""}
os.system("cls")
print("Contact Card")
print()


thisdict.update({"name":input("Input your name > ").title()})
thisdict.update({"dob":input("Input your Date of Birth (YYYY-MM-DD)> ")})
thisdict.update({"telephone":input("Input your telephone number > ")})
thisdict.update({"email":input("Input your email > ")})
thisdict.update({"address":input("Input your address > ")})
os.system("cls")
print()
print(
f"Hi {thisdict['name']}. Our dictionary says that "
f"you were born on {thisdict['dob']},"
f"we can call you on {thisdict['telephone']}," 
f"email {thisdict['email']},"
f"or write to {thisdict['address']}"
)
time.sleep(3)
