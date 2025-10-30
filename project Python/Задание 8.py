a = int(input("Введите число a: "))
n = int(input("Введите степень n: "))
result = 1
for i in range(n):
    result *= a
print (f" {a} в степени {n} = {result}")