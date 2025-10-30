n = int(input("Введите число "))
ff = 1
for i in range(1, n + 1):
   ff *= i
print(f"Факториал числа {n}! = {ff}")