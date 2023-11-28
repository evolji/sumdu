import json

def load_data():
    try:
        with open('car_data.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {'models': []}
    return data

def save_data(data):
    with open('car_data.json', 'w') as file:
        json.dump(data, file, indent=2)

def display_json_content():
    data = load_data()
    print(json.dumps(data, indent=2))

def add_car_model():
    data = load_data()

    model_name = input("Enter the car model: ")
    cost = float(input("Enter the cost of the car: "))
    age = int(input("Enter the age of the car: "))

    new_model = {'model': model_name, 'cost': cost, 'age': age}
    data['models'].append(new_model)

    save_data(data)
    print(f"{model_name} added to the JSON file.")

def remove_car_model():
    data = load_data()

    model_name = input("Enter the car model to remove: ")

    for model in data['models']:
        if model['model'] == model_name:
            data['models'].remove(model)
            save_data(data)
            print(f"{model_name} removed from the JSON file.")
            return

    print(f"Car model {model_name} not found.")

def search_by_age():
    data = load_data()

    min_age = int(input("Enter the minimum age for the search: "))

    result = [model for model in data['models'] if model['age'] > min_age]

    print("Car models with age greater than", min_age)
    print(json.dumps(result, indent=2))

def average_cost_over_six_years():
    data = load_data()

    models_over_six_years = [model for model in data['models'] if model['age'] > 6]

    if not models_over_six_years:
        print("No car models with age greater than 6 years.")
        return

    total_cost = sum(model['cost'] for model in models_over_six_years)
    average_cost = total_cost / len(models_over_six_years)

    print("Average cost of cars with age greater than 6 years:", average_cost)

while True:
    print("\n1. Display JSON content")
    print("2. Add car model")
    print("3. Remove car model")
    print("4. Search by age")
    print("5. Average cost over 6 years")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        display_json_content()
    elif choice == '2':
        add_car_model()
    elif choice == '3':
        remove_car_model()
    elif choice == '4':
        search_by_age()
    elif choice == '5':
        average_cost_over_six_years()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
