#Task 1

def main():
    input_string = "Це є довільний рядок для вправи зі зрізами."

    if len(input_string) > 8:
        slice_result = input_string[8:]
        print("Весь рядок окрім перших восьми символів:", slice_result)
    else:
        print("Довжина рядка менша за 9 символів, операція зрізу неможлива.")

if __name__ == "__main__":
    main()

#Task 2

def check_capitalized(word):
    if word and word[0].isupper():
        return True
    else:
        return False

def main():
    # Задане слово
    input_word = input("Введіть слово: ")

    # Перевірка та виведення результату
    if check_capitalized(input_word):
        print("Слово починається з великої літери.")
    else:
        print("Слово не починається з великої літери.")

if __name__ == "__main__":
    main()

#Task 3

def sort_words_by_length(sentence):
    words = sentence.split()
    sorted_words = sorted(words, key=len)

    print("Слова в порядку неспадання їх довжин:")
    for word in sorted_words:
        print(word)

def main():
    input_sentence = input("Введіть речення: ")
    sort_words_by_length(input_sentence)

if __name__ == "__main__":
    main()
