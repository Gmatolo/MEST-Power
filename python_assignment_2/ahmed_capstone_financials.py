total_amount = 50000

marketing_expense = 0.25 * total_amount
operational_expense = 0.50 * total_amount
customer_acquistion = total_amount - (marketing_expense + operational_expense)

num_of_customers = customer_acquistion / 5

print(f"budget allocated for customer_acquistion{customer_acquistion}")
print(f"Customers Acquired:{num_of_customers}")
