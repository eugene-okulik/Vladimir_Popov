import mysql.connector as mysql

db = mysql.connect(
    user="st-onl",
    passwd="AVNS_tegPDkI5BlB2lW5eASC",
    host="db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com",
    port=25060,
    database="st-onl"
)

cursor = db.cursor(dictionary=True)

insert_new_group_query = "INSERT INTO `groups` (title, start_date, end_date) " \
                         "VALUES (%s, %s, %s)"
new_group_values = (
    'German IT Students',
    'sep 2017',
    'jul 2021'
)

cursor.execute(insert_new_group_query, new_group_values)
group_id = cursor.lastrowid

insert_new_student_query = "INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)"
new_student_values = (
    'Otto',
    'Normalverbraucher',
    group_id
)
cursor.execute(insert_new_student_query, new_student_values)
student_id = cursor.lastrowid

insert_new_book_query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
insert_new_book_value = ('Python for beginners in german', student_id)
cursor.execute(insert_new_book_query, insert_new_book_value)
book1_id = cursor.lastrowid

insert_new_book_query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
insert_new_book_value = ('Java for beginners in german', student_id)
cursor.execute(insert_new_book_query, insert_new_book_value)
book2_id = cursor.lastrowid


insert_new_subject_query = "INSERT INTO subjets (title) VALUES (%s)"
insert_new_subject_value = ('Python Programming in german',)
cursor.execute(insert_new_subject_query, insert_new_subject_value)
subject1_id = cursor.lastrowid

insert_new_subject_query = "INSERT INTO subjets (title) VALUES (%s)"
insert_new_subject_value = ('Java Programming in german',)
cursor.execute(insert_new_subject_query, insert_new_subject_value)
subject2_id = cursor.lastrowid


insert_new_lessons_query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
insert_new_lessons_value = ('Python programming Lesson 1', subject1_id)
cursor.execute(insert_new_lessons_query, insert_new_lessons_value)
lesson1_id = cursor.lastrowid

insert_new_lessons_query = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
insert_new_lessons_value = ('Python programming Lesson 2', subject2_id)
cursor.execute(insert_new_lessons_query, insert_new_lessons_value)
lesson2_id = cursor.lastrowid


insert_new_marks_query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
insert_new_marks_value = (80, lesson1_id, student_id)
cursor.execute(insert_new_marks_query, insert_new_marks_value)

insert_new_marks_query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
insert_new_marks_value = (90, lesson2_id, student_id)
cursor.execute(insert_new_marks_query, insert_new_marks_value)


all_info_query = '''SELECT s.name, s.second_name, g.title as group_title, b.title as book_title,
s2.title as subj_title, l.title as lesson_title, m.value
From students s
JOIN `groups` g ON g.id = s.group_id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON s.id = m.student_id
JOIN lessons l ON m.lesson_id = l.id
JOIN subjets s2 ON l.subject_id = s2.id
WHERE s.id = %s
'''

student_id_value = (student_id, )
cursor.execute(all_info_query, student_id_value)
print(cursor.fetchall())

db.commit()
db.close()
