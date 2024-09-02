"""
THis module calculates the LOAN/
"""
LOAN = 5000
APR = 0.05

for i in range(10):
    LOAN += LOAN * APR
    print(f"LOAN total for year {i+1} is {round(LOAN,1)}")
