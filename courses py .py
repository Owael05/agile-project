courses = []

number = int(input("How many courses do you want to add? "))

for i in range(number):

    print("\n--- Add Course ---")

    code = input("Enter course code: ")
    name = input("Enter course name: ")
    classification = input("Enter classification (Core/Elective): ")

    # Validation
    if code == "" or name == "" or classification == "":
        print("Invalid information. Course was not added.")
        continue

    if (classification != "Core" and
        classification != "core" and
        classification != "Elective" and
        classification != "elective"):

        print("Invalid classification. Course was not added.")
        continue

    course = {
        "code": code,
        "name": name,
        "classification": classification
    }

    courses.append(course)

    print("Course added successfully!")

print("\n===== Course Catalog =====")

if len(courses) == 0:
    print("No courses available.")

else:
    for i in range(len(courses)):

        print("\nCourse", i + 1)
        print("Code:", courses[i]["code"])
        print("Name:", courses[i]["name"])
        print("Classification:", courses[i]["classification"])