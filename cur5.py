class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = []


class Grade:
    def __init__(self, course, assessment, mark, total_marks, feedback=""):
        self.course = course
        self.assessment = assessment
        self.mark = mark
        self.total_marks = total_marks
        self.feedback = feedback


def view_grades(student):
    print(f"\nGrades for {student.name}")
    print("-" * 40)

    # AC2: No grades yet
    if not student.grades:
        print("Not graded yet.")
        return

    # AC1: List all grades by course
    courses = {}

    for grade in student.grades:
        if grade.course not in courses:
            courses[grade.course] = []
        courses[grade.course].append(grade)

    for course, grades in courses.items():
        print(f"\nCourse: {course}")

for grade in grades:
    print(
        f"  {grade.assessment}: "
        f"{grade.mark}/{grade.total_marks}"
    )
    print(f"  Feedback: {grade.feedback}")

# Create students
student1 = Student("S001", "Mostafa Ahmed")
student2 = Student("S002", "Ahmed Ali")


# Add recorded grades for student1
student1.grades.append(
    Grade(
        "Agile Software Engineering",
        "Lab 7",
        8,
        10
    )
)

student1.grades.append(
    Grade(
        "Agile Software Engineering",
        "Lab 8",
        9,
        10
    )
)

student1.grades.append(
    Grade(
        "Database Systems",
        "Assignment 1",
        17,
        20
    )
)


# AC1: Student with recorded grades
view_grades(student1)


# AC2: Student with no grades
view_grades(student2)
