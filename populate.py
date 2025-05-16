import sqlite3

import nltk


# Step 1: Create the database and tables
def create_courses_db(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the courses table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        course_code TEXT PRIMARY KEY,
        course_name TEXT,
        units INTEGER,
        prerequisites TEXT
    )
    ''')

    # Create the elective_courses table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS elective_courses (
        course_code TEXT PRIMARY KEY,
        course_name TEXT,
        units INTEGER,
        prerequisites TEXT,
        category TEXT
    )
    ''')

    # Step 2: Insert course data
    courses_data = [
        ('عال 114', 'تراكيب محددة 1', 3, 'لا يوجد'),
        ('عال 150', 'مقدمة في برمجة الحاسبات', 4, 'لا يوجد'),
        ('نجل 140', 'اللغة الإنجليزية 1', 3, 'لا يوجد'),
        ('ريض 113', 'حساب التفاضل والتكامل التطبيقي 1', 4, 'لا يوجد'),
        ('قرا 101', 'القرآن الكريم 1', 1, 'لا يوجد'),
        # Add more courses here from your Word file...
    ]

    elective_courses_data = [
        ('نال 352', 'نظم المعلومات الجغرافية', 3, 'نال 220', 'مجموعة أنظمة الحوسبة'),
        ('نال 370', 'تفاعل الإنسان مع الحاسب', 3, 'نال 220', 'مجموعة أنظمة الحوسبة'),
        # Add more elective courses here...
    ]

    cursor.executemany(
        'INSERT OR REPLACE INTO courses (course_code, course_name, units, prerequisites) VALUES (?, ?, ?, ?)',
        courses_data)
    cursor.executemany(
        'INSERT OR REPLACE INTO elective_courses (course_code, course_name, units, prerequisites, category) VALUES (?, ?, ?, ?, ?)',
        elective_courses_data)

    conn.commit()
    conn.close()


# Step 3: Use the database in your chatbot (same as before)
def find_course_prerequisites(course_code, db_path):
    course_code = course_code.replace(' ', '').lower()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Query both the courses and elective_courses tables
    cursor.execute('SELECT prerequisites FROM courses WHERE course_code = ?', (course_code,))
    result = cursor.fetchone()

    if not result:
        cursor.execute('SELECT prerequisites FROM elective_courses WHERE course_code = ?', (course_code,))
        result = cursor.fetchone()

    conn.close()

    return result[0] if result else None


# Main chatbot function (same as before)
def chatbot(db_path):
    print("Welcome to the Course Registration Assistant!")
    print("Ask me something (e.g., 'What are the prerequisites for عال 114?') or type 'exit' to quit:")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Tokenizing the user input to extract the course code
        tokens = nltk.word_tokenize(user_input)

        # Extract course code
        course_code = None
        for token in tokens:
            if token.isalnum():  # Check if token is alphanumeric (course code)
                course_code = token
                break

        if course_code:
            prerequisites = find_course_prerequisites(course_code, db_path)

            if prerequisites:
                print(f"The prerequisites for {course_code} are: {prerequisites}")
            else:
                print("Course not found. Please check the course code or name.")
        else:
            print("Could not extract a valid course code from your query.")


# Main
if __name__ == "__main__":
    db_path = 'database.sql'  # Path to the SQLite database file
    create_courses_db(db_path)  # Create and populate the database
    chatbot(db_path)  # Run the chatbot
