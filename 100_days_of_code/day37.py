"""_summary_
"""
first_name= input("Input first name: ")
last_name = input("Input Last name: ")
new_first_name= first_name[0:3]
new_last_name = last_name[0:3]
new_f_name = (f"{first_name[0:3]}{last_name[0:3]}").title()
mother_maiden_name = input("Input mother's maiden name: ")
city = input("Input city you were born in ?: ")
new_l_name = f"{mother_maiden_name[0:2]}{city[3:]}".title()
print(f"{new_f_name} {new_l_name}")
