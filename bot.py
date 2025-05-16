import nltk
from fuzzywuzzy import process
from docx import Document

# Download the punkt tokenizer if you haven't already
nltk.download('punkt')


# Function to convert Arabic numerals to English numerals
def arabic_to_english(text):
    arabic_digits = '٠١٢٣٤٥٦٧٨٩'  # Arabic numerals
    english_digits = '0123456789'  # English numerals
    translation_table = str.maketrans(arabic_digits, english_digits)
    return text.translate(translation_table)


# Function to load course data from a Word file
def load_course_data(word_file):
    doc = Document(word_file)
    course_data = []

    for para in doc.paragraphs:
        if para.text.strip():  # Skip empty lines
            parts = para.text.split("\t")  # Assuming tab-separated values
            if len(parts) >= 4:
                course_code = arabic_to_english(parts[0].strip())  # Convert Arabic numbers to English
                course_name = parts[1].strip()
                prerequisites = parts[3].strip() if len(parts) > 3 else "No prerequisites"
                course_data.append({
                    "code": course_code,
                    "name": course_name,
                    "prerequisites": prerequisites
                })

    return course_data


# Function to find the closest matching course using fuzzy matching
def find_course(user_input, course_data):
    # Extract the course names from the course data
    course_names = [course['name'] for course in course_data]
    # Perform fuzzy matching to find the closest match
    closest_match = process.extractOne(user_input, course_names)

    if closest_match:
        course_name = closest_match[0]  # The closest matching course name
        return next(course for course in course_data if course['name'] == course_name)
    else:
        return None


# Function to handle the user input and interact with the chatbot
def chatbot(course_data):
    print("Welcome to the Course Registration Assistant!")
    print("Ask me something (e.g., 'What are the prerequisites for عال ١١٤?') or type 'exit' to quit:")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Tokenize the user input (optional step, can be expanded later)
        tokens = nltk.word_tokenize(user_input)

        # Find the closest matching course
        course = find_course(user_input, course_data)

        if course:
            print(f"The prerequisites for {course['name']} are: {course['prerequisites']}")
        else:
            print("Course not found. Please check the course code or name.")


# Load the course data from the Word file
word_file_path = r"C:\Users\Abdul\OneDrive\Desktop\Uni\GP\Web\python\db.docx"  # Replace with the actual path to your Word file
course_data = load_course_data(word_file_path)

# Start the chatbot
chatbot(course_data)
