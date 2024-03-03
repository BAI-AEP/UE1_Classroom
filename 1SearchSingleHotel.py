# L1 1
# Script-like program - sequential execution
# Variables and datatypes
# Identifier - naming conventions (must start with underscore or a letter. try starting with digits)
# Identifier - cannot be a keyword (try using class/def/pass etc.)
# Naming variables in languages other than English
# Different ways to format and print values
# Indentation (change indents and PyCharm highlights it)
# NameError - if variable misspelled (case-sensitive), not defined or used before definition
# TypeError - wrong operation (change datatype of num_days to string)


# Step 1.1: Define the details of an available Hotel (DB)
hotel_name = "Hotel Aria"
city = "Olten"
no_of_rooms = 10
stars = 4


# Step1.2: Add more details
is_available = True
price_per_night = 100.50

# Step 2: Search Hotel
# 2.1Skip
# 2.2: Search criteria
num_days = 5

# Step 3.1: Show Hotel Values
print(hotel_name)
print(city)
print(no_of_rooms)
print(stars)

# Step 3.2: Format Hotel Values
print("Name: %s" % hotel_name)
print("City: %s" % city)
print("No. of rooms: %d" % no_of_rooms)
print("Stars: %d" % stars)
print("Price per night: %f" % price_per_night)
print("Availability: %s" % is_available)

# Step 3.3: Try case-sensitivity of variable names

# Step 3.4: Calculate total price
total_price = num_days * price_per_night
print("Total price for %d days: %f" % (num_days, total_price))
# print(f"Total price for {num_days} days: {total_price}")
# print("Total price for", num_days, "days is", total_price)
# Use + operator to concatenate string
# print("Total price: " + str(total_price))
# Use + operator and % together
s = "Total price for %d days: " + str(total_price)
print(s % num_days)
print(f"No. of days for the stay: {num_days}")

