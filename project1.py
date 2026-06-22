

# Contacts = {1:"prince", 
#             2:"rahul", 
#             3:"tejas", 
#             4:"ritesh", 
#             5:"raju", 
#             6:"bheem"}

# with open("contacts.json", "w") as file:
#     json.dump(Contacts, file, indent=6)

# print("contacts saved succesfully to contacts.json!")

import json

with open("contacts.json", "r") as file:
    loaded_data = json.load(file)



print(f"Your contacts {loaded_data}")
contactsUpdate = int(input("(1)ADD (2)DELECTION (3)SEARCH (4)EXIST :-  "))
print(contactsUpdate)
while contactsUpdate in range(1,5) :
    if contactsUpdate == 1:
        contactsAddName = input("Enter the contact name :- ")
        loaded_data.update({len(loaded_data)+1:contactsAddName})
        with open("contacts.json", "w") as file:
            json.dump(loaded_data, file, indent=6)
        print(f"Your contacts {loaded_data}")
        contactsUpdate = int(input("(1)ADD (2)DELECTION (3)SEARCH (4)EXIST :-  "))
    elif contactsUpdate == 2:
        print(loaded_data)
        contactsRemove = int(input("Enter the contact serial number :-"))
        del loaded_data[str(contactsRemove)]
        print(loaded_data)
        with open("contacts.json", "w") as file:
            json.dump(loaded_data, file, indent=6)
        print(loaded_data)
        contactsUpdate = int(input("(1)ADD (2)DELECTION (3)SEARCH (4)EXIST :-  "))
    elif contactsUpdate == 3:
        varSearch = input("enter the Name:-")
        if varSearch in loaded_data.values():
            print("contact found")
            contactsUpdate = int(input("(1)ADD (2)DELECTION (3)SEARCH (4)EXIST :-  "))
        else:
            print("contact Not found")
    elif contactsUpdate == 4:
        break

    

else:
    print("Not a valid input")
    contactsUpdate = int(input("(1)ADD (2)DELECTION (3)SEARCH (4)EXIST :-  "))






        





