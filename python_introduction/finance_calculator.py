income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your monthly expenses: "))
savings_per_month = income - expenses 
Projected_Savings = savings_per_month * 12 + (savings_per_month * 12 * 0.05)
print ("Your monthly savings are $",savings_per_month,".")
print("Projected savings after one year, with interest, is: $",int(Projected_Savings),".")