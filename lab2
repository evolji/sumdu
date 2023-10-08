#Task 1

import math

def calculate_expression(x):
    numerator = 1 - 2 * math.sin(x)**2
    denominator = 1 + math.sin(x)**2
    result = numerator / denominator
    return result

def main():
    x = float(input("Введіть значення x: "))
    result = calculate_expression(x)
    print(f"Результат виразу при x={x}: {result}")

#Task 2

#my module

import math

def calculate_expression(x):
    numerator = 1 - 2 * math.sin(x)**2
    denominator = 1 + math.sin(x)**2
    result = numerator / denominator
    return result

#code

from user_module import calculate_expression

def sum_of_even_numbers(x, y):
    total_sum = 0
    for num in range(int(x), int(y) + 1):
        if num % 2 == 0:
            total_sum += num
    return total_sum

def main():
    x = float(input("Введіть значення x: "))
    y = float(input("Введіть значення y: "))

    result_expression = calculate_expression(x)
    print(f"Результат виразу при x={x}: {result_expression}")

    even_sum = sum_of_even_numbers(x, y)
    print(f"Сума парних чисел від {x} до {y}: {even_sum}")

if __name__ == "__main__":
    main()
