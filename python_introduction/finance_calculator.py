monthly_incomes = float(input("Enter your monthly income:"))
monthly_expenses = float(input("Enter your total monthly expenses:"))
monthly_savings = monthly_incomes - monthly_expenses

rate = 0.05
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * rate)

print(f"Your monthly savings is ${monthly_savings}.")
print(f"Projected savings after one year , with interest, is: ${projected_savings}.")