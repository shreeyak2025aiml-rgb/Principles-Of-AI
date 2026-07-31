# ============================================
# Utility Based Agent
# Classroom Allocation
# ============================================

classrooms = {
    "Room A": 70,
    "Room B": 90,
    "Room C": 85,
    "Room D": 60
}

print("Available Classrooms")
print("-" * 30)

for room, utility in classrooms.items():
    print(room, "Utility Score:", utility)

best = max(classrooms, key=classrooms.get)

print("\nBest Classroom")
print(best)

print("Utility Score:", classrooms[best])