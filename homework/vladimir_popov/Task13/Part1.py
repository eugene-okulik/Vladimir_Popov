import os
import datetime


base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
data_file_path = os.path.join(homework_path, "eugene_okulik", "hw_13", "data.txt")


def read_file():
    with open(data_file_path, encoding="utf-8") as file:
        for str in file.readlines():
            index_date_time, *task = str.split(" - ")
            index, date_time = index_date_time.split(". ")
            yield date_time


date_time_list = []

week_days = {1: "понедельник", 2: "вторник", 3: "среда", 4: "четверг", 5: "пятница", 6: "суббота", 7: "воскресенье"}

for date_time in read_file():
    date_time = datetime.datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S.%f")
    date_time_list.append(date_time)

first_date_time, second_date_time, third_date_time = date_time_list
now = datetime.datetime.now()

one_week_ago = first_date_time - datetime.timedelta(days=7)
week_day = datetime.datetime.isoweekday(second_date_time)
days_ago, time_ago = str(now - third_date_time).split(",")

print(one_week_ago)
print(week_days[week_day])
print(days_ago)
