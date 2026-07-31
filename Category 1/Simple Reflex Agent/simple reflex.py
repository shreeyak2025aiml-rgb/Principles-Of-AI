# ============================================
# Simple Reflex Agent
# Smart Classroom Light Controller
# ============================================

print("SMART CLASSROOM LIGHT CONTROLLER")
print("-" * 40)

while True:
    presence = input("\nAre students present? (yes/no): ").lower()

    if presence == "yes":
        print("Action: Lights ON")
    elif presence == "no":
        print("Action: Lights OFF")
    else:
        print("Invalid Input")

    choice = input("\nCheck another classroom? (yes/no): ").lower()

    if choice == "no":
        print("\nSystem Closed")
        break