
string_1 = "результат операции: 42"
string_2 = "результат операции: 514"
string_3 = "результат работы программы: 9"

colon_1_index, colon_2_index, colon_3_index = string_1.index(":"), string_2.index(":"), string_3.index(":")

digit_1 = int(string_1[colon_1_index + 1:]) + 10
digit_2 = int(string_2[colon_2_index + 1:]) + 10
digit_3 = int(string_3[colon_3_index + 1:]) + 10

print(f"{string_1[:colon_1_index + 1]} {digit_1}")
print(f"{string_2[:colon_2_index + 1]} {digit_2}")
print(f"{string_3[:colon_3_index + 1]} {digit_3}")
