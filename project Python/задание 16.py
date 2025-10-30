a = int(input("Первое число: "))
b = int(input("Второе число: "))
while b != 0:
    a, b = b, a % b
print("НОД =", a)