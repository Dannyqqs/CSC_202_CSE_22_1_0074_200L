print("Tip Calculator")

# Input: Total bill amount
while True:
    try:
        bill = float(input("How much is the total bill? $"))
        if bill <= 0:
            raise ValueError("Please enter a positive value.")
        break
    except ValueError as ve:
        print(ve)

# Input: Tip amount
while True:
    try:
        tip = float(input("How much would you like to give as a tip? $"))
        if tip < 0:
            raise ValueError("Please enter a non-negative value.")
        break
    except ValueError as ve:
        print(ve)

# Input: Number of people paying
while True:
    try:
        people = int(input("How many people are paying? "))
        if people <= 0:
            raise ValueError("Please enter a positive value.")
        break
    except ValueError as ve:
        print(ve)

# Calculate total amount including tip
total = bill + tip

# Calculate amount per person
amount_per_person = round(total / people, 2)

# Output: Display the bill, tip, number of people, and amount per person
print(f"You have a bill of ${bill:.2f} and you are giving a tip of ${tip:.2f}. "
      f"{people} people are paying, so each person will be paying ${amount_per_person:.2f}.")
