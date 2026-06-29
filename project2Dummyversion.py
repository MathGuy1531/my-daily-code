

import json
from datetime import date

with open("loaded_user_data.json", "r") as file:
    loaded_user_data = json.load(file)

# Before loop - load
with open("categories.json", "r") as file:
    categories = json.load(file)

today = str(date.today())
if today not in loaded_user_data:
    loaded_user_data[today] = {}


today_expenses = loaded_user_data[today]

print("------Welcome---User------")

mode = int(input("(1) Add expenses (2) View history (3) Exit:"))

# you can also raise an error to make it more simple

mode = int(input("(1) Add expenses (2) View history (3) Exit: "))

if mode == 3:
    exit()
elif mode == 2:
    for d, expenses in loaded_user_data.items():
        print(f"\n{d}:")
        for item, details in expenses.items():
            print(f"  {item}: {details}")
elif mode == 1:
    pass  # continues to expense adding code

    

total_expenses = 0
total_money = int(input("enter your money:- "))

while True:
    print("categories:")

    for i,cat in enumerate(categories, 1):
        print(f"{i}. {cat}")

    choice = int(input("Choose Category (-1 to add category)(0 to exit): "))
    Category = categories[choice-1]

    if choice == -1:
        AddedChoice = input("Want to Add Categories(Y/N)")
        if AddedChoice == "Y":
            AddedCategory= input("enter your category name: ")
            categories.append(AddedCategory)
            with open("categories.json", "w") as file:
                json.dump(categories, file)

            print("categories:")
            for i,cat in enumerate(categories, 1):
                print(f"{i}. {cat}")

            choice = int(input("Choose Category (0)for none: "))
            Category = categories[choice-1]
        else:
            break
    elif choice == 0:
        break
    else:
        pass

    key = input("Enter key (or type 'exit' to stop): ").strip()
    if key.lower() == 'exit':
        break
    elif key.isdigit()>0:
        print("Not a valid input!")

    try:    
        value = float(input(f"Enter value for '{key}': ").strip())
    except ValueError:
        print(f"Invalid input please enter a number")
        continue
    today_expenses[key] = {"amount": value, "category": Category, "date": today}
    with open("loaded_user_data.json", "w") as file:
            json.dump(loaded_user_data, file, indent=6)

print("\nFinal Dictionary:", today_expenses)


for i in today_expenses.values():
    total_expenses += i["amount"]

print(f"your total expenses are {total_money}/{total_money-total_expenses}")
















