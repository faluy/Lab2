while True:
    o = float(input("Число 1: "))
    v = float(input("Число 2: "))
    z = input("Операция: ")
    if z == '+': print(o + v)
    elif z == '-': print(o - v)
    elif z == '*': print(o * v)
    elif z == '/': print(o / v if v != 0 else "Ошибка")
    if input("Еще? ") == 'нет': break
    #Патриотичный код кстати, специально-_-
    