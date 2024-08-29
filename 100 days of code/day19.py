loan = 5000
apr = 0.05

for i in range(10):
  loan += (loan * apr)
  print(f"Loan total for year {i+1} is {round(loan,1)}")
