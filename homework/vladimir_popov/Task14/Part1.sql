INSERT INTO students (name, second_name, group_id) VALUES ('Max', 'Mustermann', 198)

INSERT INTO `groups` (title, start_date, end_date) VALUES ('Economics', 'sep 2017', 'jul 2021')

INSERT INTO books (title, taken_by_student_id) VALUES ('Robot Framework Level 1', 250)
INSERT INTO books (title, taken_by_student_id) VALUES ('Robot Framework Level 2', 250)
INSERT INTO books (title, taken_by_student_id) VALUES ('Robot Framework and CI/CD', 250)

INSERT INTO subjets (title) VALUES ('Programming')
INSERT INTO subjets (title) VALUES ('DB')
INSERT INTO subjets (title) VALUES ('Computer Networks')
INSERT INTO subjets (title) VALUES ('Operation Systems')

INSERT INTO lessons (title, subject_id) VALUES ('Programming Lesson 1', 261)
INSERT INTO lessons (title, subject_id) VALUES ('Programming Lesson 2', 261)

INSERT INTO lessons (title, subject_id) VALUES ('DB Basics 1', 262)
INSERT INTO lessons (title, subject_id) VALUES ('DB Basics 2', 262)

INSERT INTO lessons (title, subject_id) VALUES ('Computer Networks Basics 1', 263)
INSERT INTO lessons (title, subject_id) VALUES ('Computer Networks Basics 2', 263)

INSERT INTO lessons (title, subject_id) VALUES ('Operation Systems Windows', 264)
INSERT INTO lessons (title, subject_id) VALUES ('Operation Systems Linux', 264)

INSERT INTO marks (value, lesson_id, student_id) VALUES (90, 286, 250)
INSERT INTO marks (value, lesson_id, student_id) VALUES (85, 287, 250)

INSERT INTO marks (value, lesson_id, student_id) VALUES (80, 288, 250)
INSERT INTO marks (value, lesson_id, student_id) VALUES (80, 289, 250)

INSERT INTO marks (value, lesson_id, student_id) VALUES (75, 290, 250)
INSERT INTO marks (value, lesson_id, student_id) VALUES (100, 291, 250)

INSERT INTO marks (value, lesson_id, student_id) VALUES (75, 292, 250)
INSERT INTO marks (value, lesson_id, student_id) VALUES (80, 293, 250)


SELECT * FROM marks WHERE student_id=250
SELECT * FROM books WHERE taken_by_student_id=250
SELECT s.name, s.second_name, g.title, b.title, s2.title , l.title, m.value 
From students s
JOIN `groups` g ON g.id = s.group_id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON s.id = m.student_id 
JOIN lessons l ON m.lesson_id = l.id 
JOIN subjets s2 ON l.subject_id = s2.id 
WHERE s.id = 250
