
class Book:

    material = "бумага"
    text_availability = True

    def __init__(self, title, author, page_count, isbn, reserved):
        self.title = title
        self.author = author
        self.page_count = page_count
        self.isbn = isbn
        self.reserved = reserved
    

    def book_info(self):
        if self.reserved:
            print(f"Название: {self.title}, Автор: {self.author}, страниц: {self.page_count}, материал: {self.material}, зарезервирована")
        else:
            print(f"Название: {self.title}, Автор: {self.author}, страниц: {self.page_count}, материал: {self.material}")


book_1 = Book("Идиот", "Достоевский", 500, 12345, False)
book_2 = Book("Три товарища", "Ремарк", 300, 23456, False)
book_3 = Book("Сто лет одиночества", "Маркес", 600, 34567, False)
book_4 = Book("Анна Каренина", "Толстой", 700, 45678, True)
book_5 = Book("Братья Карамазовы", "Достоевский", 500, 56789, False)

book_1.book_info()
book_2.book_info()
book_3.book_info()
book_4.book_info()
book_5.book_info()


class School_Book(Book):

    def __init__(self, title, author, page_count, isbn, reserved, subject, school_class, tasks_availability):
        super().__init__(title, author, page_count, isbn, reserved)
        self.subject = subject
        self.school_class = school_class
        self.tasks_availability = tasks_availability


    def book_info(self):
        if self.reserved:
            print(f"Название: {self.title}, Автор: {self.author}, страниц: {self.page_count}, предмет: {self.subject}, класс: {self.school_class}, зарезервирована")
        else:
            print(f"Название: {self.title}, Автор: {self.author}, страниц: {self.page_count}, предмет: {self.subject}, класс: {self.school_class}")


school_book1 = School_Book(title="Алгебра", author="Иванов", page_count=200, isbn=12345, tasks_availability=True, subject="Математика", school_class=9, reserved=False)
school_book2 = School_Book(title="История Казахстана", author="Алимов", page_count=250, isbn=23456, tasks_availability=False, subject="История", school_class=9, reserved=True)
school_book3 = School_Book(title="English", author="Петров", page_count=150, isbn=34567, tasks_availability=True, subject="Английский язык", school_class=6, reserved=False)

school_book1.book_info()
school_book2.book_info()
school_book3.book_info()
