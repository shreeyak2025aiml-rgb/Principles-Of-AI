# ============================================
# Goal Based Agent
# Campus Navigation Robot
# ============================================

goal = input("Enter Destination: ")

current = input("Enter Current Location: ")

while current != goal:

    print("\nRobot Moving...")
    print("Current Location:", current)

    current = input("Enter New Location: ")

print("\nDestination Reached Successfully")
print("Goal Achieved")