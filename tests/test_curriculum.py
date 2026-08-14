"""
Unit tests for the Curriculum Module.

Tests:
CUR-01: Add a Course
CUR-02: Enroll in a Course
CUR-03: Create an Assessment
CUR-04: Record a Grade
CUR-05: View Grades and Feedback
"""

import unittest
from io import StringIO
from contextlib import redirect_stdout

from curriculum import (
    Course,
    Student,
    Assessment,
    add_course,
    enroll_in_course,
    create_assessment,
    record_grade,
    view_grades,
)


class TestCUR01AddCourse(unittest.TestCase):

    def setUp(self):
        self.catalog = []

    def test_add_core_course(self):
        result = add_course(
            self.catalog,
            "CSE101",
            "Introduction to Programming",
            "Core"
        )

        self.assertTrue(result)
        self.assertEqual(len(self.catalog), 1)
        self.assertEqual(self.catalog[0].classification, "Core")

    def test_add_elective_course(self):
        result = add_course(
            self.catalog,
            "CSE450",
            "Artificial Intelligence",
            "Elective"
        )

        self.assertTrue(result)
        self.assertEqual(len(self.catalog), 1)
        self.assertEqual(self.catalog[0].classification, "Elective")

    def test_missing_course_code_is_rejected(self):
        result = add_course(
            self.catalog,
            "",
            "Database Systems",
            "Core"
        )

        self.assertFalse(result)
        self.assertEqual(len(self.catalog), 0)

    def test_missing_course_name_is_rejected(self):
        result = add_course(
            self.catalog,
            "CSE102",
            "",
            "Core"
        )

        self.assertFalse(result)
        self.assertEqual(len(self.catalog), 0)

    def test_invalid_classification_is_rejected(self):
        result = add_course(
            self.catalog,
            "CSE103",
            "Database Systems",
            "Invalid"
        )

        self.assertFalse(result)
        self.assertEqual(len(self.catalog), 0)


class TestCUR02Enrollment(unittest.TestCase):

    def setUp(self):
        self.catalog = [
            Course("CSE101", "Introduction to Programming", "Core", True),
            Course("CSE102", "Data Structures", "Core", True),
            Course("CSE103", "Database Systems", "Core", False),
        ]
        self.student = Student("S001", "Mostafa Ahmed")

    def test_enroll_in_available_course(self):
        result = enroll_in_course(
            self.student,
            self.catalog[0]
        )

        self.assertTrue(result)
        self.assertIn(
            self.catalog[0],
            self.student.enrolled_courses
        )

    def test_unavailable_course_is_rejected(self):
        result = enroll_in_course(
            self.student,
            self.catalog[2]
        )

        self.assertFalse(result)
        self.assertNotIn(
            self.catalog[2],
            self.student.enrolled_courses
        )

    def test_duplicate_enrollment_is_rejected(self):
        enroll_in_course(
            self.student,
            self.catalog[0]
        )

        result = enroll_in_course(
            self.student,
            self.catalog[0]
        )

        self.assertFalse(result)
        self.assertEqual(
            self.student.enrolled_courses.count(self.catalog[0]),
            1
        )


class TestCUR03Assessment(unittest.TestCase):

    def setUp(self):
        self.course = Course(
            "CSE233",
            "Agile Software Engineering",
            "Core"
        )

    def test_create_valid_assessment(self):
        result = create_assessment(
            self.course,
            "A01",
            "Lab 7",
            "Custom Workflows and Transition Rules",
            10
        )

        self.assertTrue(result)
        self.assertEqual(len(self.course.assessments), 1)
        self.assertEqual(
            self.course.assessments[0].title,
            "Lab 7"
        )

    def test_empty_title_is_rejected(self):
        result = create_assessment(
            self.course,
            "A01",
            "",
            "Missing title test",
            10
        )

        self.assertFalse(result)
        self.assertEqual(len(self.course.assessments), 0)

    def test_empty_description_is_rejected(self):
        result = create_assessment(
            self.course,
            "A01",
            "Lab 7",
            "",
            10
        )

        self.assertFalse(result)
        self.assertEqual(len(self.course.assessments), 0)

    def test_invalid_total_marks_is_rejected(self):
        result = create_assessment(
            self.course,
            "A01",
            "Lab 7",
            "Invalid marks test",
            0
        )

        self.assertFalse(result)
        self.assertEqual(len(self.course.assessments), 0)


class TestCUR04RecordGrade(unittest.TestCase):

    def setUp(self):
        self.course = Course(
            "CSE233",
            "Agile Software Engineering",
            "Core"
        )

        self.student = Student(
            "S001",
            "Mostafa Ahmed"
        )

        self.assessment = Assessment(
            "A01",
            "Lab 7",
            "Custom Workflows",
            10,
            self.course
        )

    def test_valid_grade_is_recorded(self):
        result = record_grade(
            self.student,
            self.assessment,
            8
        )

        self.assertTrue(result)
        self.assertEqual(len(self.student.grades), 1)
        self.assertEqual(self.student.grades[0].mark, 8)

    def test_zero_grade_is_valid(self):
        result = record_grade(
            self.student,
            self.assessment,
            0
        )

        self.assertTrue(result)

    def test_maximum_grade_is_valid(self):
        result = record_grade(
            self.student,
            self.assessment,
            10
        )

        self.assertTrue(result)

    def test_grade_above_maximum_is_rejected(self):
        result = record_grade(
            self.student,
            self.assessment,
            15
        )

        self.assertFalse(result)
        self.assertEqual(len(self.student.grades), 0)

    def test_negative_grade_is_rejected(self):
        result = record_grade(
            self.student,
            self.assessment,
            -1
        )

        self.assertFalse(result)
        self.assertEqual(len(self.student.grades), 0)

    def test_feedback_is_saved_with_grade(self):
        result = record_grade(
            self.student,
            self.assessment,
            8,
            "Good work"
        )

        self.assertTrue(result)
        self.assertEqual(
            self.student.grades[0].feedback,
            "Good work"
        )


class TestCUR05ViewGrades(unittest.TestCase):

    def test_student_with_grades_can_view_grades(self):
        course = Course(
            "CSE233",
            "Agile Software Engineering",
            "Core"
        )

        student = Student(
            "S001",
            "Mostafa Ahmed"
        )

        assessment = Assessment(
            "A01",
            "Lab 7",
            "Custom Workflows",
            10,
            course
        )

        record_grade(
            student,
            assessment,
            8,
            "Good work"
        )

        output = StringIO()

        with redirect_stdout(output):
            view_grades(student)

        result = output.getvalue()

        self.assertIn(
            "Agile Software Engineering",
            result
        )
        self.assertIn(
            "Lab 7",
            result
        )
        self.assertIn(
            "8/10",
            result
        )

    def test_feedback_is_displayed(self):
        course = Course(
            "CSE233",
            "Agile Software Engineering",
            "Core"
        )

        student = Student(
            "S001",
            "Mostafa Ahmed"
        )

        assessment = Assessment(
            "A01",
            "Lab 7",
            "Custom Workflows",
            10,
            course
        )

        record_grade(
            student,
            assessment,
            8,
            "Good work"
        )

        output = StringIO()

        with redirect_stdout(output):
            view_grades(student)

        result = output.getvalue()

        self.assertIn(
            "Feedback: Good work",
            result
        )

    def test_student_without_grades_sees_not_graded_yet(self):
        student = Student(
            "S002",
            "Ahmed Ali"
        )

        output = StringIO()

        with redirect_stdout(output):
            view_grades(student)

        result = output.getvalue()

        self.assertIn(
            "Not graded yet.",
            result
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
