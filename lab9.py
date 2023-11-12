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

create_file('TF15_1.txt', lines)

find_symmetric_words('TF15_1.txt', 'TF15_2.txt')

print_words('TF15_2.txt')
