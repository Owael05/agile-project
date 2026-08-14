spaces = []

number = int(input("How many spaces do you want to add? "))

for i in range(number):
    print("\n--- Add Space ---")

    name = input("Enter space name: ")
    space_type = input("Enter type (classroom/lab): ")
    capacity = int(input("Enter capacity: "))
    equipment = input("Enter equipment: ")

    # Validation
    if name == "" or space_type == "" or equipment == "" or capacity <= 0:
        print("Invalid information. Space was not added.")
        continue

    if space_type != "classroom" and space_type != "lab":
        print("Invalid type. Space was not added.")
        continue

    space = {
        "name": name,
        "type": space_type,
        "capacity": capacity,
        "equipment": equipment
    }

    spaces.append(space)

    print("Space added successfully!")

print("\n===== Available Spaces =====")

if len(spaces) == 0:
    print("No spaces available.")
else:
    for i in range(len(spaces)):
        print("\nSpace", i + 1)
        print("Name:", spaces[i]["name"])
        print("Type:", spaces[i]["type"])
        print("Capacity:", spaces[i]["capacity"])
        print("Equipment:", spaces[i]["equipment"])