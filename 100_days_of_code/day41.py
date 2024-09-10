"""
Website rating
"""

# website = {"name": None, "url": None, "desc": None, "rating": None}

# for name in website.keys():
#   website[name] = input(f"{name}: ")

# print()
# for name, value in website.items():
#   print(f"{name}: {value}")

print("Website Rating")

thisdict = {"name": "", "url": "", "desc": "", "rating": ""}

thisdict.update({"name":input("Input the Website name: ")})
thisdict.update({"url": input("Input the URL: ")})
thisdict.update({"desc":input("Input a description: ")})
thisdict.update({"rating":input("Input a star rating: ")})

for name, value in thisdict.items():
    print(f"{name}: {value},", end = " "  )
