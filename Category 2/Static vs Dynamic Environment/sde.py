import random
import time

print("=" * 50)
print("STATIC VS DYNAMIC ENVIRONMENT")
print("=" * 50)

choice = input("Choose Environment (static/dynamic): ").lower()

parking_slots = 10

if choice == "static":

    print("\nParking Slots:", parking_slots)

else:

    print("\nDynamic Parking Status\n")

    for i in range(5):

        parking_slots += random.randint(-2, 2)

        if parking_slots < 0:
            parking_slots = 0

        print("Available Slots:", parking_slots)

        time.sleep(1)