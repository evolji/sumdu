#Task 1
import numpy as np
import matplotlib.pyplot as plt

def Y(x):
    return 5 * np.sin(10 * x) * np.sin(3 * x) / (x**x)

x_values = np.linspace(0.01, 8, 400)  
y_values = Y(x_values)

plt.plot(x_values, y_values, linestyle='-', color='blue', linewidth=2, label='Y(x)=5*sin(10*x)*sin(3*x)/(x^x)')

plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.title('Графік функції Y(x)=5*sin(10*x)*sin(3*x)/(x^x)')
plt.xlabel('x')
plt.ylabel('Y(x)')
plt.legend()
plt.show()

#Task 2
import csv
import matplotlib.pyplot as plt

file_path = 'Data.csv'  

years = []
ukraine_capital_ratio = []
uk_capital_ratio = []

with open(file_path, 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader) 
    try:
        selected_country = input("Введіть назву країни для побудови діаграми: ")
        selected_country_index = header.index(f'2008 [YR2008]')
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row[0] == selected_country: 
                    years = [int(year.split()[0]) for year in header[4:]] 
                    selected_country_data = [float(value) for value in row[4:]] 
                    break
        plt.figure(figsize=(10, 5))
        plt.plot(years, selected_country_data, label=selected_country, marker='o')
        plt.title(f'Динаміка Bank capital to assets ratio для {selected_country} за 2008-2022 роки')
        plt.xlabel('Рік')
        plt.ylabel('Bank capital to assets ratio (%)')
        plt.legend()
        plt.show()
    except ValueError as e:
        print(f"Помилка: {e}")

#Task 3
import matplotlib.pyplot as plt
def is_symmetric(word):
    return word == word[::-1]

def create_file(filename, lines):
    with open(filename, 'w') as file:
        file.write('\n'.join(lines))

def find_symmetric_words(input_filename, output_filename):
    symmetric_words = []

    with open(input_filename, 'r') as input_file:
        content = input_file.read().split()

        for word in content:
            if is_symmetric(word):
                symmetric_words.append(word)

    with open(output_filename, 'w') as output_file:
        output_file.write(' '.join(symmetric_words))

def print_words(filename):
    with open(filename, 'r') as file:
        content = file.read().split()
        for word in content:
            print(word)

lines = [
    "абввба",
    "різної",
    "довжини",
    "слова",
    "в",
    "яких",
    "розділені",
    "пробілами",
    "і",
    "розділовими",
    "знаками"
]
def build_pie_chart(symmetric_words, content):
    symmetric_percentage = len(symmetric_words) / len(content) * 100
    non_symmetric_percentage = 100 - symmetric_percentage

    data = {'Симетричні слова': symmetric_percentage, 'Несиметричні слова': non_symmetric_percentage}

    labels = list(data.keys())
    values = list(data.values())

    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99'])
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Кругова діаграма симетричних слів')

    plt.show()

symmetric_words = []
content = []

find_symmetric_words('TF15_1.txt', 'TF15_2.txt')

with open('TF15_1.txt', 'r') as file:
    content = file.read().split()

with open('TF15_2.txt', 'r') as file:
    symmetric_words = file.read().split()

build_pie_chart(symmetric_words, content)
