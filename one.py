import nltk
from fuzzywuzzy import process
from docx import Document

# Step 1: Download the necessary NLTK data for tokenizing
nltk.download('punkt')


# Step 2: Load courses from the Word file
def load_courses_from_word(file_path):
    courses = {}
    doc = Document(file_path)
    for para in doc.paragraphs:
        # Assuming each line has the course code and prerequisites
        if para.text.strip():  # To avoid empty lines
            # Replace Arabic numbers with English numbers
            para_text = para.text.translate(str.maketrans('٠١٢٣٤٥٦٧٨٩', '0123456789'))
            course_info = para_text.split('-')
            if len(course_info) >= 2:
                course_code = course_info[0].strip()
                prerequisites = course_info[1].strip()
                courses[course_code] = prerequisites
    return courses


# Step 3: Fuzzy search for courses in the document
def find_course_prerequisites(course_code, courses):
    course_code = course_code.replace(' ', '').lower()  # Normalize the input
    choices = [key.lower() for key in courses.keys()]

    # Use fuzzywuzzy to find the best match
    matched_course, score = process.extractOne(course_code, choices)

    if score >= 80:  # If the match score is high enough, return the course info
        return courses[matched_course]
    else:
        return None


# Step 4: Main chatbot function
def chatbot(course_data):
    print("Welcome to the Course Registration Assistant!")
    print("Ask me something (e.g., 'What are the prerequisites for عال 114?') or type 'exit' to quit:")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Tokenizing the user input to extract the course code
        tokens = nltk.word_tokenize(user_input)

        # Extract course code (assuming it's the course name/number)
        course_code = None
        for token in tokens:
            if token.isalnum():  # Check if token is alphanumeric (e.g., course code)
                course_code = token
                break

        if course_code:
            prerequisites = find_course_prerequisites(course_code, course_data)

            if prerequisites:
                print(f"The prerequisites for {course_code} are: {prerequisites}")
            else:
                print("Course not found. Please check the course code or name.")
        else:
            print("Could not extract a valid course code from your query.")


# Step 5: Run the chatbot with the courses from the Word file
if __name__ == "__main__":
    file_path = 'data.docx'  # Path to the updated data file
    courses = load_courses_from_word(file_path)

    if courses:
        chatbot(courses)
    else:
        print("No courses found in the Word document.")
