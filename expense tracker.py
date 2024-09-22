my_dict = {}

while True:
    key = input("Enter the Expense serial number (or type 'quit' to exit): ")
    if key.lower() == 'quit':
        break
    value = float(input("Enter the amount here: "))
    my_dict[key] = value

user_input = input('What would you like me to do: ')
values_list = list(my_dict.values())

def monthly_budget(budget):
    entries = 0
    while entries < 30 and budget > 0:
        expense = float(input("Enter the expense amount: "))
        if budget < expense:
            print("You cannot afford this, try something cheaper")
        else:
            budget -= expense
            entries += 1
        print("Your new budget is", budget)

if user_input.lower() == 'please summarize my expenses':
    total_expenses = sum(my_dict.values())
    print(f"Total expenses: {total_expenses}")

elif user_input.lower() == 'i would like to delete an expense':
    key_to_delete = input("Enter the Expense serial number to delete: ")
    if key_to_delete in my_dict:
        my_dict.pop(key_to_delete)
        print("You deleted " + key_to_delete)
    else:
        print("Expense serial number not found.")

elif user_input.lower() == 'show me all my expenses':
    print(values_list)

elif user_input.lower() == 'set budget':
    budget = float(input("Enter your budget: "))
    monthly_budget(budget)
