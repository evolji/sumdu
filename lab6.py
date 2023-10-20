#Task 1

def insert_odd_elements(list_to_modify, new_elements):
  for i in range(1, len(list_to_modify), 2):
    list_to_modify.insert(i, new_elements[i - 1])
  return list_to_modify

def main():
  list_to_modify = input("Введіть список: ").split()
  new_elements = input("Введіть список нових елементів: ").split()
  modified_list = insert_odd_elements(list_to_modify, new_elements)
  print("Модифікований список: ", modified_list)

if __name__ == "__main__":
  main()

#Task 2

def swap_max_min(list_to_modify):
  max_index = list_to_modify.index(max(list_to_modify))
  min_index = list_to_modify.index(min(list_to_modify))
  list_to_modify[max_index], list_to_modify[min_index] = list_to_modify[min_index], list_to_modify[max_index]
  return list_to_modify

def main():
  list_to_modify = input("Введіть список: ").split()
  modified_list = swap_max_min(list_to_modify)
  print("Модифікований список: ", modified_list)

if __name__ == "__main__":
  main()

#Task 3

def process_word(word):
    char_set = set(word)
    first_occurrences = []

    for char in word:
        if char not in first_occurrences:
            first_occurrences.append(char)
            char_set.add(char)

    print("Перші входження літер:", first_occurrences)
    print("Множина:", char_set)

input_word = input("Введіть слово з латинських літер: ")
process_word(input_word)
