"""
Curriculum Module
Agile Software Engineering Project

Covers:
CUR-01: Add a Course
CUR-02: Enroll in a Course
CUR-03: Create an Assessment
CUR-04: Record a Grade
CUR-05: View Grades and Feedback
"""


class Course:
    def __init__(self, course_id, name, classification="Core", available=True):
        self.course_id = course_id
        self.name = name
        self.classification = classification.capitalize()
        self.available = available
        self.assessments = []

    def __str__(self):
        return f"{self.course_id} - {self.name} ({self.classification})"


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.enrolled_courses = []
        self.grades = []

    def __str__(self):
        return f"{self.student_id} - {self.name}"


class Assessment:
    def __init__(self, assessment_id, title, description, total_marks, course):
        self.assessment_id = assessment_id
        self.title = title
        self.description = description
        self.total_marks = total_marks
        self.course = course

    def __str__(self):
        return f"{self.title} ({self.total_marks} marks)"


class Grade:
    def __init__(self, student, assessment, mark, feedback=""):
        self.student = student
        self.assessment = assessment
        self.course = assessment.course
        self.mark = mark
        self.total_marks = assessment.total_marks
        self.feedback = feedback

    def __str__(self):
        return f"{self.assessment.title}: {self.mark}/{self.total_marks}"


# ============================================================
# CUR-01: ADD COURSE
# ============================================================

def add_course(catalog, course_id, name, classification):
    if not course_id.strip():
        print("Validation Error: Course code is required.")
        return False

    if not name.strip():
        print("Validation Error: Course name is required.")
        return False

    if classification.strip().lower() not in ["core", "elective"]:
        print("Validation Error: Classification must be Core or Elective.")
        return False

    classification = classification.strip().capitalize()

    course = Course(
        course_id.strip(),
        name.strip(),
        classification
    )

    catalog.append(course)

    print(f"Course '{course.name}' added successfully.")
    print(f"Classification: {course.classification}")

    return True


def view_course_catalog(catalog):
    print("\n===== Course Catalog =====")

    if not catalog:
        print("No courses available.")
        return

    for course in catalog:
        status = "Available" if course.available else "Unavailable"
        print(
            f"{course.course_id} - {course.name} | "
            f"{course.classification} | {status}"
        )


# ============================================================
# CUR-02: ENROLL IN COURSE
# ============================================================

def view_available_courses(catalog):
    print("\n===== Available Courses =====")

    available_courses = [
        course for course in catalog
        if course.available
    ]

    if not available_courses:
        print("No available courses.")
        return

    for course in available_courses:
        print(
            f"{course.course_id} - {course.name} "
            f"({course.classification})"
        )


def enroll_in_course(student, course):
    if course in student.enrolled_courses:
        print("Error: You are already enrolled in this course.")
        return False

    if not course.available:
        print("Error: This course is not available.")
        return False

    student.enrolled_courses.append(course)

    print(
        f"{student.name} successfully enrolled in {course.name}."
    )

    return True


def view_student_courses(student):
    print(f"\n===== Courses for {student.name} =====")

    if not student.enrolled_courses:
        print("No enrolled courses.")
        return

    for course in student.enrolled_courses:
        print(
            f"- {course.course_id}: {course.name} "
            f"({course.classification})"
        )


# ============================================================
# CUR-03: CREATE ASSESSMENT
# ============================================================

def create_assessment(
    course,
    assessment_id,
    title,
    description,
    total_marks
):
    if not assessment_id.strip():
        print("Validation Error: Assessment ID is required.")
        return False

    if not title.strip():
        print("Validation Error: Assessment title is required.")
        return False

    if not description.strip():
        print("Validation Error: Assessment description is required.")
        return False

    if total_marks <= 0:
        print("Validation Error: Total marks must be greater than 0.")
        return False

    assessment = Assessment(
        assessment_id.strip(),
        title.strip(),
        description.strip(),
        total_marks,
        course
    )

    course.assessments.append(assessment)

    print(
        f"Assessment '{assessment.title}' created successfully."
    )
    print(f"Linked to course: {course.name}")

    return True


def view_assessments(course):
    print(f"\n===== Assessments: {course.name} =====")

    if not course.assessments:
        print("No assessments available.")
        return

    for assessment in course.assessments:
        print(
            f"- {assessment.assessment_id}: "
            f"{assessment.title} "
            f"({assessment.total_marks} marks)"
        )


# ============================================================
# CUR-04: RECORD A GRADE
# ============================================================

def record_grade(student, assessment, mark, feedback=""):
    if mark < 0 or mark > assessment.total_marks:
        print(
            f"Validation Error: Mark must be between "
            f"0 and {assessment.total_marks}."
        )
        return False

    grade = Grade(
        student,
        assessment,
        mark,
        feedback.strip()
    )

    student.grades.append(grade)

    print("Grade recorded successfully.")
    print(f"Student: {student.name}")
    print(f"Assessment: {assessment.title}")
    print(f"Mark: {mark}/{assessment.total_marks}")

    if feedback.strip():
        print(f"Feedback: {feedback.strip()}")

    return True


# ============================================================
# CUR-05: VIEW GRADES AND FEEDBACK
# ============================================================

def view_grades(student):
    print(f"\n===== Grades for {student.name} =====")
    print("-" * 50)

    if not student.grades:
        print("Not graded yet.")
        return

    courses = {}

    for grade in student.grades:
        course_name = grade.course.name

        if course_name not in courses:
            courses[course_name] = []

        courses[course_name].append(grade)

    for course_name, grades in courses.items():
        print(f"\nCourse: {course_name}")

        for grade in grades:
            print(
                f"  {grade.assessment.title}: "
                f"{grade.mark}/{grade.total_marks}"
            )
            print(
                f"  Feedback: "
                f"{grade.feedback if grade.feedback else 'No feedback'}"
            )


def demo():
    catalog = []

    add_course(
        catalog,
        "CSE101",
        "Introduction to Programming",
        "Core"
    )

    add_course(
        catalog,
        "CSE450",
        "Artificial Intelligence",
        "Elective"
    )

    view_course_catalog(catalog)

    student = Student("S001", "Mostafa Ahmed")

    view_available_courses(catalog)
    enroll_in_course(student, catalog[0])
    enroll_in_course(student, catalog[0])

    assessment_created = create_assessment(
        catalog[0],
        "A01",
        "Lab 7",
        "Custom Workflows and Transition Rules",
        10
    )

    if assessment_created:
        record_grade(
            student,
            catalog[0].assessments[0],
            8,
            "Good work. Keep improving."
        )

        view_grades(student)

    student_without_grades = Student("S002", "Ahmed Ali")
    view_grades(student_without_grades)


if __name__ == "__main__":
    demo()
