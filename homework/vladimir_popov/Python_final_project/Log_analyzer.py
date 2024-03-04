import argparse
import os
from os import listdir
from datetime import datetime
from colorama import Fore, Style


class LogAnalyzer:
    def __init__(self, dir_file_name, date, text, unwanted_text, fulltext):
        self.dir_file_name = dir_file_name
        self.date = date
        self.text = text
        self.unwanted_text = unwanted_text
        self.fulltext = fulltext
        self.file_path = self.find_file()

    def find_file(self):
        self.base_path = os.path.dirname(__file__)
        self.homework_path = os.path.dirname(os.path.dirname(self.base_path))
        base_path = os.path.join(self.homework_path, "eugene_okulik", "data")

        for root, dirs, files in os.walk(base_path):
            if self.dir_file_name in files:
                file_path = os.path.join(root, self.dir_file_name)
                yield file_path
            elif self.dir_file_name in dirs:
                dir_path = os.path.join(root, self.dir_file_name)
                for file in listdir(dir_path):
                    file_path = os.path.join(dir_path, file)
                    yield file_path

    def create_blocks_from_file(self, file_path):
        current_date = None
        error_text = []
        file_blocks = {}

        with open(file_path, encoding="utf-8") as file:
            for line in file.readlines():
                try:
                    date_match = str(datetime.strptime(line[:23], '%Y-%m-%d %H:%M:%S.%f'))[:-3]
                    if current_date:
                        file_blocks[current_date] = error_text
                        error_text = []
                    current_date = date_match
                    error_text.append(line.strip())
                except:
                    error_text.append(line.strip())

            if current_date:
                file_blocks[current_date] = error_text

        return file_blocks

    def create_blocks(self):
        for file_path in self.find_file():
            log_block = self.create_blocks_from_file(file_path)
            yield log_block

    def find_log(self):
        logs_date = []
        logs_text = []
        logs_extext = []

        if self.date:
            logs_date = self.find_log_by_date()
        if self.text:
            logs_text = self.find_by_text()
        if self.unwanted_text:
            logs_extext = self.exclude_text()

        if logs_text:
            if logs_date and logs_text:
                if logs_date and logs_text and logs_extext:
                    for block in self.create_blocks():
                        for key, value in block.items():
                            value = ' '.join(value)
                            if key in logs_text:
                                if key in logs_date:
                                    if key in logs_extext:
                                        start_word_index = value.index(self.text)
                                        end_word_index = start_word_index + len(self.text)

                                        if len(value[:start_word_index]) > 150:
                                            start = start_word_index - 150
                                        else:
                                            start = start_word_index - len(value[:start_word_index])

                                        end = end_word_index + 150

                                        print(
                                        f'{Fore.LIGHTMAGENTA_EX} [{key}] {Style.RESET_ALL}'
                                        f'{value[start:start_word_index]}'
                                        f'{Style.BRIGHT}{Fore.LIGHTGREEN_EX}{self.text}'
                                        f'{Style.RESET_ALL}{value[end_word_index:end]}'
                                        )
                else:   
                    for block in self.create_blocks():
                        for key, value in block.items():
                            value = ' '.join(value)
                            if key in logs_text:
                                if key in logs_date:
                                    start_word_index = value.index(self.text)
                                    end_word_index = start_word_index + len(self.text)

                                    if len(value[:start_word_index]) > 150:
                                        start = start_word_index - 150
                                    else:
                                        start = start_word_index - len(value[:start_word_index])

                                    end = end_word_index + 150

                                    print(
                                    f'{Fore.LIGHTMAGENTA_EX} [{key}] {Style.RESET_ALL}'
                                    f'{value[start:start_word_index]}'
                                    f'{Style.BRIGHT}{Fore.LIGHTGREEN_EX}{self.text}'
                                    f'{Style.RESET_ALL}{value[end_word_index:end]}'
                                    )
            elif logs_text and logs_extext:
                for block in self.create_blocks():
                    for key, value in block.items():
                        value = ''.join(value)
                        if key in logs_text:
                            if key in logs_extext:
                                start_word_index = value.index(self.text)
                                end_word_index = start_word_index + len(self.text)

                                if len(value[:start_word_index]) > 150:
                                    start = start_word_index - 150
                                else:
                                    start = start_word_index - len(value[:start_word_index])

                                end = end_word_index + 150

                                print(
                                f'{Fore.LIGHTMAGENTA_EX} [{key}] {Style.RESET_ALL}'
                                f'{value[start:start_word_index]}'
                                f'{Style.BRIGHT}{Fore.LIGHTGREEN_EX}{self.text}'
                                f'{Style.RESET_ALL}{value[end_word_index:end]}'
                                )
            else: 
                for block in self.create_blocks():
                    for key, value in block.items():
                        value = ' '.join(value)
                        if key in logs_text:
                            start_word_index = value.index(self.text)
                            end_word_index = start_word_index + len(self.text)

                            if len(value[:start_word_index]) > 150:
                                start = start_word_index - 150
                            else:
                                start = start_word_index - len(value[:start_word_index])

                            end = end_word_index + 150

                            print(
                            f'{Fore.LIGHTMAGENTA_EX} [{key}] {Style.RESET_ALL}'
                            f'{value[start:start_word_index]}'
                            f'{Style.BRIGHT}{Fore.LIGHTGREEN_EX}{self.text}'
                            f'{Style.RESET_ALL}{value[end_word_index:end]}'
                            )
        elif logs_date:
            if logs_date and logs_extext:
                for block in self.create_blocks():
                    for key, value in block.items():
                        value = ''.join(value)
                        if key in logs_date:
                            if key in logs_extext:
                                print(f"{Fore.LIGHTMAGENTA_EX} [{key}] {Style.RESET_ALL} {''.join(value)[:300]}")
            else: 
                for block in self.create_blocks():
                    for key, value in block.items():
                        value = ''.join(value)
                        if key in logs_date:
                            print(f"{Fore.LIGHTMAGENTA_EX} [{key}] {Style.RESET_ALL} {''.join(value)[:300]}")  
        elif logs_extext:
            for block in self.create_blocks():
                for key, value in block.items():
                    if key in logs_extext:
                        print(
                        f'{Fore.LIGHTMAGENTA_EX} [{key}] {Style.RESET_ALL}'
                        f'{value[:300]}'
                        )

    def find_by_text(self):
        log_by_text_list = []

        for log_block in self.create_blocks():
            for key, value in log_block.items():
                value = ' '.join(value)
                if self.text in value:
                    log_by_text_list.append(key)

        return log_by_text_list

    def find_log_by_date(self):
        date_found = False
        log_by_date_list = []
        try:
            try:
                border1, border2 = self.date.split('/')
                for log_block in self.create_blocks():
                    for key, value in log_block.items():
                        try:
                            border1 = str(datetime.strptime(border1[:23], '%Y-%m-%d %H:%M:%S.%f'))[:-3]
                            border2 = str(datetime.strptime(border2[:23], '%Y-%m-%d %H:%M:%S.%f'))[:-3]
                            if key >= border1 and key <= border2:
                                date_found = True
                                if self.fulltext == "True":
                                        log_by_date_list.append(key)
                                else:
                                        log_by_date_list.append(key)
                        except:
                            if border1 == "..":
                                if key <= border2:
                                    date_found = True
                                    if self.fulltext == "True":
                                        log_by_date_list.append(key)
                                    else:
                                        log_by_date_list.append(key)
                            if border2 == "..":
                                if key >= border1:
                                    date_found = True
                                    if self.fulltext == "True":
                                        log_by_date_list.append(key)
                                    else:
                                        log_by_date_list.append(key)
            except:
                for log_block in self.create_blocks():
                    if self.fulltext == "True":
                        log_by_date_list.append(key)
                    else:
                        log_by_date_list.append(key)
                    date_found = True
        except:
            if date_found == False:
                print(f'Logs with date {Fore.RED} {self.date} {Style.RESET_ALL} not found')

        return log_by_date_list

    def exclude_text(self):
        exclude_text_list = []
        results_count = 0
        logs_count = 0
        for log_block in self.create_blocks():
            for key, value in log_block.items():
                value = ' '.join(value)
                logs_count += 1
                if self.unwanted_text not in value:
                    results_count += 1
                    exclude_text_list.append(key)

        return exclude_text_list


parser = argparse.ArgumentParser()
parser.add_argument('file', help='File name')
parser.add_argument('-d', '--date', help='Datetime for search: less than: "../2022-01-13 00:00:00.000", '
                    'more than: "2022-01-13 00:00:00.000/..", from - '
                    'to "2022-01-13 00:00:00.000/2022-01-14 00:00:00.000", '
                    'exact: 2022-01-13 00:00:00.000'
                    )
parser.add_argument('-t', '--text', help='A text to look for')
parser.add_argument('-n', '--unwanted', help='A text to filter out logs')
parser.add_argument('-f', '--fulltext', help='Return full log text')
args = parser.parse_args()

log_analyser = LogAnalyzer(args.file, args.date, args.text, args.unwanted, args.fulltext)
log_analyser.find_log()
