from random import random, randint, choice

salary = int(input("Введите зарплату: "))

bonus = choice([True, False])

if bonus:
    print(f"${salary + randint(0, 500)}")
else:
    print(f"${salary}")
