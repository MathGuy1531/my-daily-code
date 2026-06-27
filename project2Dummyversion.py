

import json

total_money = int(input("enter your money:- "))
total_expenses = 0

with open("loaded_user_data.json", "r") as file:
    loaded_user_data = json.load(file)


while True:
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
    loaded_user_data[key] = value
    with open("loaded_user_data.json", "w") as file:
            json.dump(loaded_user_data, file, indent=6)

print("\nFinal Dictionary:", loaded_user_data)


for i in loaded_user_data.values():
    total_expenses += i

print(f"your total expenses are {total_money}/{total_money-total_expenses}")
















