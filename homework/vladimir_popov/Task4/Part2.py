
string_1 = "результат операции: 42"
string_2 = "результат операции: 514"
string_3 = "результат работы программы: 9"

digit_1 = int(string_1.split(":")[1]) + 10
digit_2 = int(string_2.split(":")[1]) + 10
digit_3 = int(string_3.split(":")[1]) + 10

print(f"{string_1.split(':')[0]} : {digit_1}")
print(f"{string_2.split(':')[0]} : {digit_2}")
print(f"{string_3.split(':')[0]} : {digit_3}")
