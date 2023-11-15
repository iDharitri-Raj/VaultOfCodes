# Initialize an empty inventory dictionary to store items and their quantities.
inventory = {}

# Function to add a new item to the inventory.


def add_item():
    item_name = input("Enter the name of the item: ")
    quantity = int(input("Enter the quantity: "))
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity
    print(f"{quantity} {item_name}(s) added to the inventory.")

# Function to update an existing item's quantity.


def update_item():
    item_name = input("Enter the name of the item to update: ")
    if item_name in inventory:
        new_quantity = int(input("Enter the new quantity: "))
        inventory[item_name] = new_quantity
        print(f"{item_name} quantity updated to {new_quantity}.")
    else:
        print(f"{item_name} is not in the inventory.")

# Function to view the current inventory.


def view_inventory():
    print("Current Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

# Function to remove an item from the inventory.


def remove_item():
    item_name = input("Enter the name of the item to remove: ")
    if item_name in inventory:
        del inventory[item_name]
        print(f"{item_name} removed from the inventory.")
    else:
        print(f"{item_name} is not in the inventory.")


# Main program loop.
while True:
    print("\nGrocery Store Inventory Management")
    print("1. Add Item")
    print("2. Update Item Quantity")
    print("3. View Inventory")
    print("4. Remove Item")
    print("5. Quit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        add_item()
    elif choice == "2":
        update_item()
    elif choice == "3":
        view_inventory()
    elif choice == "4":
        remove_item()
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4/5).")
