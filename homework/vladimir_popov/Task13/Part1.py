import os
import datetime


base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
data_file_path = os.path.join(homework_path, "eugene_okulik", "hw_13", "data.txt")


def read_file():
    with open(data_file_path, encoding="utf-8") as file:
        for str in file.readlines():
            index_date_time, *task = str.split(" - ")
            yield index_date_time.split(". ")


date_time_list = []

week_days = {1: "понедельник", 2: "вторник", 3: "среда", 4: "четверг", 5: "пятница", 6: "суббота", 7: "воскресенье"}

now = datetime.datetime.now()

for index, date_time in read_file():
    date_time = datetime.datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S.%f")
    if int(index) == 1:
        print(date_time + datetime.timedelta(days=7))
    elif int(index) == 2:
        print(week_days[datetime.datetime.isoweekday(date_time)])
    elif int(index) == 3:
        days_ago, time_ago = str(now - date_time).split(",")
        print(days_ago)

