# PyPassword Generator

import string
import random

print("Welcome to the PyPassword Generator!")

# Define character sets
capital_letters = string.ascii_uppercase
small_letters = string.ascii_lowercase
symbols = string.punctuation
digits = string.digits

# Combine all character sets
combo = capital_letters + small_letters + symbols + digits

# Shuffle the character set to make it more secure
shuffled_combo = random.sample(combo, len(combo))

# Input: User specifies the length of the password
while True:
    try:
        length = int(input("How long do you want your password to be? "))
        if length <= 0:
            raise ValueError("Please enter a positive integer.")
        break
    except ValueError as ve:
        print(ve)

# Generate the password
password = ''.join(random.choices(shuffled_combo, k=length))

print("Your password is:", password)