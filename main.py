import spacy
from docx import Document
import sys
sys.stdout.reconfigure(encoding='utf-8')


# Function to extract data from the Word file
def extract_data_from_word(file_path):
    doc = Document(file_path)
    course_data = {}

    # Process the paragraphs in the document
    course_name = ""
    prerequisites = ""

    for para in doc.paragraphs:
        # Identify the start of a course entry (this could be based on the title 'رمز المقرر' or 'اسم المقرر')
        if "رمز المقرر" in para.text:
            if course_name and prerequisites:
                course_data[course_name] = prerequisites
            course_name = ""
            prerequisites = ""
        
        if "اسم المقرر" in para.text:
            course_name = para.text.split("اسم المقرر")[-1].strip()
        
        if "المتطلبات" in para.text:
            prerequisites = para.text.split("المتطلبات")[-1].strip()

    if course_name and prerequisites:  # Add last course
        course_data[course_name] = prerequisites

    return course_data

# Function to process the user's query and extract the course name
def get_course_prerequisite(query, course_data):
    query = query.strip()  # Clean up any extra spaces or characters
    course_name = None

    # Attempt to match the course name directly (case insensitive)
    for course in course_data:
        if course_name := course.strip() == query.strip():
            return course_data[course_name]

    return "Sorry, I couldn't find the prerequisites for that course. Please specify a valid course."

# Main chatbot loop
def chatbot():
    # Load your course data
    course_data = extract_data_from_word('db.docx')  # Replace with your Word file path
    
    print("Hello! I am your Registration Assistant. You can ask about course prerequisites.")
    while True:
        query = input("You: ")
        if query.lower() in ['exit', 'quit', 'bye']:
            print("Goodbye!")
            break
        answer = get_course_prerequisite(query, course_data)
        print(f"Chatbot: {answer}")

print("حلول")
# Run the chatbot
if __name__ == "__main__":
    chatbot()
