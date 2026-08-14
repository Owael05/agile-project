class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = []


class Assessment:
    def __init__(self, assessment_id, title, total_marks, course):
        self.assessment_id = assessment_id
        self.title = title
        self.total_marks = total_marks
        self.course = course


class Grade:
    def __init__(self, student, assessment, mark):
        self.student = student
        self.assessment = assessment
        self.mark = mark


def record_grade(student, assessment, mark):

    # AC2: Validate mark range
    if mark < 0 or mark > assessment.total_marks:
        print(
            f"Validation Error: Mark must be between "
            f"0 and {assessment.total_marks}."
        )
        return False

    # AC1: Save grade and link it to the student and assessment
    grade = Grade(student, assessment, mark)
    student.grades.append(grade)

    print(f"Grade recorded successfully.")
    print(f"Student: {student.name}")
    print(f"Assessment: {assessment.title}")
    print(f"Course: {assessment.course}")
    print(f"Mark: {mark}/{assessment.total_marks}")

    return True


# Course
course = "Agile Software Engineering"

# Enrolled student
student = Student("S001", "Mostafa Ahmed")

# Assessment
assessment = Assessment(
    "A01",
    "Lab 7",
    10,
    course
)


# AC1: Record a valid grade
record_grade(student, assessment, 8)


# AC2: Try to record an invalid grade
record_grade(student, assessment, 15)


# Display student's grades
print("\nStudent Grades:")

for grade in student.grades:
    print(
        f"{grade.assessment.title}: "
        f"{grade.mark}/{grade.assessment.total_marks}"
    )