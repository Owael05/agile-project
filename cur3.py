class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name
        self.assessments = []


class Assessment:
    def __init__(self, title, description, total_marks):
        self.title = title
        self.description = description
        self.total_marks = total_marks


def create_assessment(course, title, description, total_marks):
    # AC2: Validate required fields
    if not title.strip():
        print("Validation Error: Assessment title is required.")
        return False

    if not description.strip():
        print("Validation Error: Assessment description is required.")
        return False

    if total_marks <= 0:
        print("Validation Error: Total marks must be greater than 0.")
        return False

    # AC1: Create and link assessment to the course
    assessment = Assessment(title, description, total_marks)
    course.assessments.append(assessment)

    print(f"Assessment '{title}' created successfully.")
    print(f"Linked to course: {course.name}")

    return True


# Course taught by the professor
course = Course("CSE233", "Agile Software Engineering")


# AC1: Create a valid assessment
create_assessment(
    course,
    "Lab 7",
    "Custom Workflows and Transition Rules",
    10
)


# AC2: Try to create an invalid assessment
create_assessment(
    course,
    "",
    "Missing title test",
    10
)


# Display assessments linked to the course
print("\nAssessments in the course:")

for assessment in course.assessments:
    print(f"- {assessment.title}: {assessment.total_marks} marks")