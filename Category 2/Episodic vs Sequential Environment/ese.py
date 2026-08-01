print("=" * 50)
print("EPISODIC VS SEQUENTIAL ENVIRONMENT")
print("=" * 50)

choice = input("Choose Environment (episodic/sequential): ").lower()

if choice == "episodic":

    marks = int(input("Enter Today's Quiz Marks: "))

    if marks >= 50:
        print("Result: PASS")
    else:
        print("Result: FAIL")

else:

    total = 0

    for i in range(3):

        marks = int(input(f"Enter Quiz {i+1} Marks: "))
        total += marks

    average = total / 3

    print("\nAverage Marks:", average)

    if average >= 50:
        print("Overall Result: PASS")
    else:
        print("Overall Result: FAIL")