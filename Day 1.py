# BandName Generator
# Combining the name of an animal and a city

print("BandName Generator")

# Input: User enters the name of their favorite city
city = input("Enter the name of your favorite city: ")

# Input: User enters the name of any animal
animal = input("Enter the name of an animal: ")

# Combining the city name and animal name to form the band name
band_name = city.capitalize() + " " + animal.capitalize()

# Output: Displaying the generated band name
print("Your band name could be: " + band_name)
