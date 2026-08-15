
class Course:
    def __init__(self, course_id, name, available=True):
        self.course_id = course_id
        self.name = name
        self.available = available


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.enrolled_courses = []


def view_available_courses(catalog):
    print("\nAvailable Courses:")
    for course in catalog:
        if course.available:
            print(f"{course.course_id} - {course.name}")


def enroll_in_course(student, course):
    # AC3: Prevent duplicate enrollment
    if course in student.enrolled_courses:
        print("Error: You are already enrolled in this course.")
        return False

    # AC2: Course must be available
    if not course.available:
        print("Error: This course is not available.")
        return False

    # Create enrollment and link it to the student
    student.enrolled_courses.append(course)
    print(f"Successfully enrolled in {course.name}.")
    return True


# Course catalog
catalog = [
    Course("CSE101", "Introduction to Programming"),
    Course("CSE102", "Data Structures"),
    Course("CSE103", "Database Systems", available=False),
    Course("CSE104", "Software Engineering")
]

# Student
student = Student("S001", "Mostafa Ahmed")

# AC1: View available courses
view_available_courses(catalog)

# AC2: Enroll in an available course
enroll_in_course(student, catalog[0])

# AC3: Try to enroll in the same course again
enroll_in_course(student, catalog[0])

# Display student's enrolled courses
print("\nStudent's Enrolled Courses:")
for course in student.enrolled_courses:
    print(f"- {course.course_id}: {course.name}")

