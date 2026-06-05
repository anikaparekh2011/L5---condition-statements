actual_cost = float(input("Enter the cost you bought the item at: "))
selling_cost = float(input("Enter the cost you sold the item at: "))

if selling_cost > actual_cost:
    profit = selling_cost - actual_cost
    print("You have gained",profit ,"amount")
else: 
    print("No profit made!!")