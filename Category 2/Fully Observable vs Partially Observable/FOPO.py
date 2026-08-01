import random

print("=" * 50)
print("FULLY OBSERVABLE VS PARTIALLY OBSERVABLE")
print("=" * 50)

rooms = {
    "Library": "Safe",
    "Laboratory": "Smoke Detected",
    "Cafeteria": "Crowded",
    "Parking": "Safe"
}

choice = input("Choose Environment (fully/partially): ").lower()

if choice == "fully":
    print("\nAgent can observe the entire campus.\n")

    for room, status in rooms.items():
        print(f"{room} --> {status}")

else:
    print("\nAgent can observe only one location.\n")

    location = random.choice(list(rooms.keys()))
    print(f"{location} --> {rooms[location]}")