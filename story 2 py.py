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

print("===== Search Facility Availability =====")

date = input("Enter date (DD/MM/YYYY): ")
time = input("Enter time (HH:MM): ")
minimum_capacity = int(input("Enter minimum capacity: "))

found = False

print("\n===== Available Spaces =====")

for space in spaces:

    # Check capacity
    if space["capacity"] < minimum_capacity:
        continue

    # Check if the space is booked
    booked = False

    for reservation in reservations:

        if (reservation["space"] == space["name"] and
            reservation["date"] == date and
            reservation["time"] == time):

            booked = True
            break

    if not booked:
        print("Name:", space["name"])
        print("Type:", space["type"])
        print("Capacity:", space["capacity"])
        print("----------------------")

        found = True

if not found:
    print("No available spaces found.")