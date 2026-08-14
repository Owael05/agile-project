spaces = [
    {"name": "Room101", "type": "classroom", "capacity": 30},
    {"name": "Room202", "type": "classroom", "capacity": 50},
    {"name": "Lab1", "type": "lab", "capacity": 25},
    {"name": "Lab2", "type": "lab", "capacity": 40}
]

reservations = [
    {"space": "Room101", "date": "15/08/2026", "time": "10:00"},
    {"space": "Lab2", "date": "15/08/2026", "time": "12:00"}
]

print("===== Reserve a Facility =====")

space_name = input("Enter space name: ")
date = input("Enter date (DD/MM/YYYY): ")
time = input("Enter time (HH:MM): ")

# Check if space exists
space_exists = False

for space in spaces:
    if space["name"] == space_name:
        space_exists = True
        break

if not space_exists:
    print("Space does not exist.")

else:

    # Check for reservation conflict
    conflict = False

    for reservation in reservations:

        if (reservation["space"] == space_name and
            reservation["date"] == date and
            reservation["time"] == time):

            conflict = True
            break

    if conflict:
        print("Reservation failed!")
        print("This space is already reserved for this date and time.")

    else:
        new_reservation = {
            "space": space_name,
            "date": date,
            "time": time
        }

        reservations.append(new_reservation)

        print("Reservation created successfully!")
        print("Space:", space_name)
        print("Date:", date)
        print("Time:", time)