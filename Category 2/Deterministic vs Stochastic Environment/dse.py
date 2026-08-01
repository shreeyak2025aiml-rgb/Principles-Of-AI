import random

print("=" * 50)
print("DETERMINISTIC VS STOCHASTIC")
print("=" * 50)

choice = input("Choose Environment (deterministic/stochastic): ").lower()

attendance = 80

if choice == "deterministic":

    print("\nAttendance:", attendance)

    if attendance >= 75:
        print("Eligible for Exam")
    else:
        print("Not Eligible")

else:

    attendance += random.randint(-20, 20)

    print("\nToday's Attendance:", attendance)

    if attendance >= 75:
        print("Eligible for Exam")
    else:
        print("Not Eligible")