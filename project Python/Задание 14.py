balance = 1000
while balance > 0:
    print(f"Баланс: {balance} руб.")
    take = int(input("Сколько снять: "))
    if take <= balance:
        balance -= take
    else:
        print("Недостаточно средств")
print("Деньги закончились")