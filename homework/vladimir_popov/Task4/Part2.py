
string_1 = "результат операции: 42"
string_2 = "результат операции: 514"
string_3 = "результат работы программы: 9"

digit_1_index = string_1.split().index("42")
digit_2_index = string_2.split().index("514")
digit_3_index = string_3.split().index("9")

digit_1 = int(string_1.split()[digit_1_index]) + 10
digit_2 = int(string_2.split()[digit_2_index]) + 10
digit_3 = int(string_3.split()[digit_3_index]) + 10

print(f"{' '.join(string_1.split()[:digit_1_index])} {digit_1}")
print(f"{' '.join(string_2.split()[:digit_2_index])} {digit_2}")
print(f"{' '.join(string_3.split()[:digit_3_index])} {digit_3}")
