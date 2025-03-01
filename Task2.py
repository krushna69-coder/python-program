items = {
    "Laptop": 45000,
    "Headphones": 2000,
    "Smartphone": 15000,
    "Charger": 500,
    "Tablet": 25000
}

print("WELCOME TO STUDENT ELECTRONICS ")
print("\nAvailable Items:")
print("\n Laptop - Rs. 45000 \n Headphones - Rs. 2000 \n Smartphone - Rs. 15000 \n Charger - Rs. 500 \n Tablet - Rs. 25000")


item_name = input("\nWhat do you want to buy? ") 


if item_name in items: 
    quantity = int(input("How many units do you want to buy? ")) 
    print(f"Total cost for {quantity} {item_name}(s) is Rs. {quantity * items[item_name]}.")
else: 
    print("Sorry, we don't have that item in stock.")