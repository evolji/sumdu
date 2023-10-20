#Task 1

N = int(input("Введіть довжину масиву: "))

arr = []
for i in range(N):
    element = int(input(f"Введіть елемент масиву #{i + 1}: "))
    arr.append(element)

negative_elements = [el for el in arr if el < 0]
negative_elements.reverse()

print("Від'ємні елементи у зворотньому порядку:", negative_elements)


#Task 2

def fill_array(array):
  for i in range(-7, 0):
    for j in range(len(array[0])):
      array[i][j] = (i+1) + j

array = [[0] * 7 for _ in range(7)]
fill_array(array)

print(*array, sep='\n')
