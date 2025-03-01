items = {
    "AndroidTV": 55000,
    "Washing Machine": 45000,
    "AC": 57000,
    "Smartphone": 25000,
    "Oven": 12000,
    "Fridge": 42000
}

print("WELCOME TO STUDENT ELECTRONICS")


purchased_items = []

while True:
    
    print("\nAvailable Products:")
    for item, price in items.items():
        print(f" {item} : Rs {price}")

    item_name = input("\nWhat would you like to buy?: ").strip()

    if item_name in items:
        try:
            
            quantity = int(input("How many quantity you want to purchase?: "))
            if quantity <= 0:
                print("Quantity must be a positive number.")
                continue

            
            total_cost = quantity * items[item_name]
            purchased_items.append((item_name, quantity, total_cost))
            print(f"Added {quantity} {item_name}(s) for a total of Rs {total_cost}.")
        except ValueError:
            print("Please enter a valid number for quantity.")
            continue
    else:
        print("Sorry, we don't have that item in stock.")

    
    another = input("Do you want to buy anything more? (yes or no): ").strip().lower()
    if another != "yes":
        break


print("\nBill Summary")
grand_total = 0
for item, qty, cost in purchased_items:
    print(f"{qty} {item}(s) total: Rs {cost}")
    grand_total += cost

print(f"\nYour total bill is Rs {grand_total}")
print("Thank you for shopping with us!")



# WELCOME TO STUDENT ELECTRONICS

# Available Products:
#  AndroidTV : Rs 55000
#  Washing Machine : Rs 45000
#  AC : Rs 57000
#  Smartphone : Rs 25000
#  Oven : Rs 12000
#  Fridge : Rs 42000

# What would you like to buy?: AC
# How many quantity you want to purchase?: 65
# Added 65 AC(s) for a total of Rs 3705000.
# Do you want to buy anything more? (yes or no): yes

# Available Products:
#  AndroidTV : Rs 55000
#  Washing Machine : Rs 45000
#  AC : Rs 57000
#  Smartphone : Rs 25000
#  Oven : Rs 12000
#  Fridge : Rs 42000

# What would you like to buy?: Oven
# How many quantity you want to purchase?: 600
# Added 600 Oven(s) for a total of Rs 7200000.
# Do you want to buy anything more? (yes or no): no

# Bill Summary
# 65 AC(s) total: Rs 3705000
# 600 Oven(s) total: Rs 7200000

# Your total bill is Rs 10905000
# Thank you for shopping with us!