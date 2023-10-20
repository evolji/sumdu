#Task 1

print("Enter")
a = int(input("a = "))
b = int(input("b = "))
while(a < 1 or a > 100 or b < 1 or b > 100):
     print("Error!")
     a = int(input("a = "))
     b = int(input("b = "))
if a < b:
    x = (b/a)+1
elif a == b:
    x = 25
elif a > b:
    x = ((a*a*a)-5)/b

print("x = %f" %x)

#Task 2

import math
print("Число | Квадратний корінь")
print("-" * 25)
for i in range(1, 101):
    print(f"{i:5} | {math.sqrt(i):.2f}")

#Task 3

n = int(input("Введіть ціле число n від 1 до 9: "))
if 1 < n < 9:
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print() 
else:
    print("error")
