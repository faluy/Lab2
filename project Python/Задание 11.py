import random

number = random.randint(1, 10)

while True:
    guess = int(input("Угадай число от 1 до 10: "))
    if guess == number:
        print("Угадал!")
        break
    elif guess < number:
        print("Больше")
    else:
        print("Меньше")