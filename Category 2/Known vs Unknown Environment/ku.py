import random

print("=" * 50)
print("KNOWN VS UNKNOWN ENVIRONMENT")
print("=" * 50)

choice = input("Choose Environment (known/unknown): ").lower()

known_route = [
    "College Gate",
    "Admin Block",
    "Library"
]

if choice == "known":

    print("\nFollowing Known Route\n")

    for place in known_route:
        print("Moving to:", place)

    print("\nDestination Reached")

else:

    print("\nUnknown Environment")

    places = [
        "Parking",
        "Playground",
        "Cafeteria",
        "Library"
    ]

    while True:

        current = random.choice(places)

        print("Exploring:", current)

        if current == "Library":
            print("Destination Found")
            break