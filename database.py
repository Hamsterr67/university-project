"""
Модуль для работы с базой данных "Студенческая группа".
"""
import sqlite3

def get_connection():
    """Возвращает соединение с базой данных."""
    return sqlite3.connect('university.db')

def init_database():
    """Создаёт таблицы в базе данных."""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        last_name TEXT NOT NULL,
        first_name TEXT NOT NULL,
        student_card TEXT UNIQUE NOT NULL,
        group_name TEXT NOT NULL,
        phone TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_name TEXT NOT NULL,
        teacher TEXT NOT NULL,
        hours INTEGER DEFAULT 72
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        subject_id INTEGER NOT NULL,
        grade_date DATE NOT NULL,
        grade_value INTEGER NOT NULL,
        status TEXT DEFAULT 'выставлена',
        FOREIGN KEY (student_id) REFERENCES students (id),
        FOREIGN KEY (subject_id) REFERENCES subjects (id)
    )
    ''')
    
    conn.commit()
    conn.close()
    print("База данных 'Студенческая группа' успешно инициализирована!")

if __name__ == "__main__":
    init_database()
