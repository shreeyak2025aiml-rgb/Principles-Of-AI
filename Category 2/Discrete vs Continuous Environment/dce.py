import random

print("=" * 50)
print("DISCRETE VS CONTINUOUS ENVIRONMENT")
print("=" * 50)

choice = input("Choose Environment (discrete/continuous): ").lower()

if choice == "discrete":

    temperature = random.choice([
        "LOW",
        "MEDIUM",
        "HIGH"
    ])

    print("\nTemperature Level:", temperature)

else:

    temperature = round(random.uniform(20.0, 40.0), 2)

    print("\nCurrent Temperature:", temperature, "°C")