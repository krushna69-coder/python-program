cars = [
    {"type": "SUV", "deposit": 15000, "rent": 5000, "models": ["Ford Everest", "Jeep Cherokee", "Nissan Patrol", "Volkswagen Touareg"]},
    {"type": "Sedan", "deposit": 10000, "rent": 4000, "models": ["Mazda 6", "Audi A4", "BMW 3 Series", "Mercedes C-Class"]},
    {"type": "MPV", "deposit": 20000, "rent": 6000, "models": ["Honda Odyssey", "Chrysler Pacifica", "Toyota Sienna", "Renault Espace"]}
]

rented_cars = []
def display_cars():
    print("\nAvailable Cars:")
    for car in cars:
        print(f"{car['type']}: {', '.join(car['models'])} | Rent: ₹{car['rent']}/day, Deposit: ₹{car['deposit']}")

def rent_car():
    display_cars()
    car_type = int(input("\nSelect car type (1-SUV, 2-Sedan, 3-MPV): ")) - 1
    if car_type not in range(len(cars)):
        print("Invalid choice.")
        return

    selected_car = cars[car_type]
    for i, model in enumerate(selected_car['models'], 1):
        print(f"{i}. {model}")

    model_index = int(input("Select model number: ")) - 1
    if model_index not in range(len(selected_car['models'])):
        print("Invalid choice.")
        return

    rental_days = int(input(f"Enter rental days for {selected_car['models'][model_index]}: "))
    rented_cars.append({
        "model": selected_car['models'][model_index],
        "type": selected_car['type'],
        "rent": rental_days * selected_car['rent'],
        "deposit": selected_car['deposit']
    })
    print(f"{selected_car['models'][model_index]} rented for ₹{rental_days * selected_car['rent']} (Rent) + ₹{selected_car['deposit']} (Deposit)")

while True:
    print("\n1. Show Cars\n2. Rent a Car\n3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        display_cars()
    elif choice == "2":
        rent_car()
    elif choice == "3":
        print("\nRented Cars:")
        for car in rented_cars:
            print(f"Model: {car['model']}, Type: {car['type']}, Rent Paid: ₹{car['rent']}, Deposit: ₹{car['deposit']}")
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")


#output

# 1. Show Cars
# 2. Rent a Car
# 3. Exit
# Enter your choice: 2

# Available Cars:
# SUV: Ford Everest, Jeep Cherokee, Nissan Patrol, Volkswagen Touareg | Rent: ₹5000/day, Deposit: ₹15000
# Sedan: Mazda 6, Audi A4, BMW 3 Series, Mercedes C-Class | Rent: ₹4000/day, Deposit: ₹10000
# MPV: Honda Odyssey, Chrysler Pacifica, Toyota Sienna, Renault Espace | Rent: ₹6000/day, Deposit: ₹20000

# Select car type (1-SUV, 2-Sedan, 3-MPV): 1
# 1. Ford Everest
# 2. Jeep Cherokee
# 3. Nissan Patrol
# 4. Volkswagen Touareg
# Select model number: 1
# Enter rental days for Ford Everest: 2
# Ford Everest rented for ₹10000 (Rent) + ₹15000 (Deposit)

# 1. Show Cars
# 2. Rent a Car
# 3. Exit
# Enter your choice: 2

# Available Cars:
# SUV: Ford Everest, Jeep Cherokee, Nissan Patrol, Volkswagen Touareg | Rent: ₹5000/day, Deposit: ₹15000
# Sedan: Mazda 6, Audi A4, BMW 3 Series, Mercedes C-Class | Rent: ₹4000/day, Deposit: ₹10000
# MPV: Honda Odyssey, Chrysler Pacifica, Toyota Sienna, Renault Espace | Rent: ₹6000/day, Deposit: ₹20000

# Select car type (1-SUV, 2-Sedan, 3-MPV): 3
# 1. Honda Odyssey
# 2. Chrysler Pacifica
# 3. Toyota Sienna
# 4. Renault Espace
# Select model number: 2
# Enter rental days for Chrysler Pacifica: 2
# Chrysler Pacifica rented for ₹12000 (Rent) + ₹20000 (Deposit)

# 1. Show Cars
# 2. Rent a Car
# 3. Exit
# Enter your choice: 3

# Rented Cars:
# Model: Ford Everest, Type: SUV, Rent Paid: ₹10000, Deposit: ₹15000
# Model: Chrysler Pacifica, Type: MPV, Rent Paid: ₹12000, Deposit: ₹20000
# Goodbye!