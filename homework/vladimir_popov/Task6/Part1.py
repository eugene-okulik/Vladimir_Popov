
secret_digit = 3

print("Угадайте цифру")

while True:
    user_digit = int(input("Введите цифру: "))

    if user_digit != secret_digit:
        print("Попробуйте снова")
    elif user_digit == secret_digit:
        print("Поздравляю! Вы угадали!")
        break
