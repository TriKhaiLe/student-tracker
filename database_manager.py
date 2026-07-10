import sqlite3

from student import Student

class DatabaseManager:
    def __init__(self, db_name="students.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                math REAL NOT NULL,
                literature REAL NOT NULL,
                english REAL NOT NULL,
                average REAL NOT NULL,
                rank TEXT NOT NULL
            )
        ''')
        self.conn.commit()

    def add_student(self, student):
        self.cursor.execute("INSERT INTO students (name, age, math, literature, english, average, rank) VALUES (?, ?, ?, ?, ?, ?, ?)",
                            (student.name, student.age, student.math, student.literature, student.english, student.average, student.rank))
        self.conn.commit()

    def delete_student(self, student_id):
        self.cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
        self.conn.commit()
        
    def get_all_students(self):
        students = []

        self.cursor.execute("SELECT * FROM students")
        rows = self.cursor.fetchall()
        for row in rows:
            student = Student(name=row[1], age=row[2], math=row[3], literature=row[4], english=row[5], student_id=row[0], average=row[6], rank=row[7])
            students.append(student)

        return students

