
temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23
]

hot_days = list(filter(lambda x: x > 28, temperatures))

hottest_day = max(hot_days)
average_day = round(sum(hot_days) / len(hot_days))
coldest_day = min(hot_days)

print(hottest_day)
print(average_day)
print(coldest_day)
