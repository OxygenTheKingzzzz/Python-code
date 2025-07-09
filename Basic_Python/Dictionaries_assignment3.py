# Exercise 3
data = {
 'January': {'sales': 1000, 'expenses': 400},
 'February': {'sales': 1200, 'expenses': 500},
 'March': {'sales': 900, 'expenses': 450}
}
"""
Write a program to:
• Compute and print the total sales and total expenses for the quarter.
• Also calculate the profit (sales - expenses) for each month.
"""
total_sales=0
total_expense=0
for key,value in data.items():
    """
    You're declaring variables (sales and expenses) to store and access values from another dictionary 
    (value in this case), which comes from a nested dictionary structure.

    """
    sale=value['sales']
    expense=value['expenses']
    total_expense=total_sales-total_expense
    profit=sale-expense
    total_sales+=sale
    total_expense+=expense
    print(f"{key}: Profit = {profit} \t total sales={total_sales} \t total expense={total_expense}")