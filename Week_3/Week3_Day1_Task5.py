#Task 5: Store Inventory Update.
#Create a dictionary called store with items and their available quantities.

# Available items
store = {}
items = ["Phones", "Tabs", "Chargers", "Watches"]

# Available quantities
quantities = [100, 150, 86, 125]
print("The following are the available items: ")
store = {items[0]: quantities[0], items[1]: quantities[1], items[2]: quantities[2], items[3]: quantities[3]}
before_purchase = {item: quantity for item, quantity in store.items()}
print(store)

# Ask the user to input the item they want to buy
item_needed = input("\nEnter the item you need: ")

# Ask the user to input the quantity they want to purchase.
quant_needed = int(input("Enter quantity needed: "))

# Use the assignment operator (-=) to update (reduce) the item quantity in the dictionary.
store[item_needed] -= quant_needed
print(store)

# Print the updated dictionary
print(f"\n\t===Updated Dictionary===\nBefore purchase: {before_purchase}")
print(f"After purchase: {store}")