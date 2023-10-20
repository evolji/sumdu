cars = {
    "model_1": (100000, 2020),
    "model_2": (200000, 2019),
    "model_3": (300000, 2018),
    "model_4": (400000, 2017),
    "model_5": (500000, 2016),
    "model_6": (600000, 2015),
    "model_7": (700000, 2014),
    "model_8": (800000, 2013),
    "model_9": (900000, 2012),
    "model_10": (1000000, 2011),
}

def print_all_values():
    for key, value in cars.items():
        print(f"{key}: {value}")

def add_new_record():
    model = input("Введіть назву моделі автомобіля: ")
    price = int(input("Введіть вартість автомобіля: "))
    year = int(input("Введіть рік випуску автомобіля: "))
    cars[model] = (price, year)

def delete_record():
    model = input("Введіть назву моделі автомобіля, яку потрібно видалити: ")
    del cars[model]

def view_sorted_keys():
    for key in sorted(cars.keys()):
        print(key)

def calculate_average_price():
    total_price = 0
    car_count = 0
    for key, value in cars.items():
        age = 2023 - value[1]
        if age > 6:
            total_price += value[0]
            car_count += 1
    return total_price / car_count

while True:
    print("Виберіть дію:")
    print("1. Вивести всі значення словника")
    print("2. Додати новий запис")
    print("3. Видалити запис")
    print("4. Перегляд вмісту словника за відсортованими ключами")
    print("5. Визначення середньої вартості автомобілів, вік яких перевищує 6 років")
    print("6. Вийти")
    action = input("Введіть номер дії: ")

    if action == "1":
        print_all_values()
    elif action == "2":
        add_new_record()
    elif action == "3":
        delete_record()
    elif action == "4":
        view_sorted_keys()
    elif action == "5":
        print(calculate_average_price())
    elif action == "6":
        break
