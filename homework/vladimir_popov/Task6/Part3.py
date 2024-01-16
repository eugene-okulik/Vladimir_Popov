
def plus_ten(str):
    text, digit =  str.split(":")
    print(f"{text}: {int(digit) + 10}")

plus_ten("результат операции: 42")
plus_ten("результат операции: 54")
plus_ten("результат работы программы: 209")
plus_ten("результат: 2")
