import dotenv
import os
import csv
import mysql.connector as mysql

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
data_file_path = os.path.join(homework_path, "eugene_okulik", "Lesson_16", "hw_data", "data.csv")

dotenv.load_dotenv()

db = mysql.connect(
   user=os.getenv('DB_USER'),
   passwd=os.getenv('DB_PASSW'),
   host=os.getenv('DB_HOST'),
   port=os.getenv('DB_PORT'),
   database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True, buffered=True)

with open(data_file_path) as csv_file:
    file_data = csv.DictReader(csv_file)
    data = []
    for row in file_data:
        student_name = row['name']
        select_student_query = "SELECT id FROM students WHERE name = %s"
        select_student_value = (student_name,)
        cursor.execute(select_student_query, select_student_value)
        student_id = cursor.fetchone()

        if not student_id:
            print(f'There is no info for student with name {student_name}')
        else:
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
            student_id = (student_id['id'],)
            cursor.execute(all_info_query, student_id)
            print(cursor.fetchall())

db.close()
