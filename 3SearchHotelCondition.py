# L1 3
# Display hotel based on availability
# Conditions if/else
# Boolean operators
# No need of operator for boolean variable

# Step 1.1: Define the details of a Hotel (DB)
hotel_name = "Hotel Aria"
city = "Olten"
no_of_rooms = 10
stars = 4
is_available = False
price_per_night = 100.50


# Step 2: Search Hotel
# Step 2.1Skip

# Step 3: Show available hotels

# Step 3.1: Define a function to show available hotel details
# try is_available == True
# is_available != False
# try is_available
# try syntax error if is_available = True:
def show_available_hotels():
    if is_available == True:
        print("Name: %s" % hotel_name)
        print("City: %s" % city)
        print("No. of rooms: %d" % no_of_rooms)
        print("Stars: %d" % stars)
        print("Price per night: %.2f" % price_per_night)
    else:
        print("Sorry, no hotels have available rooms at the moment :(")


# Step 3.2: Call the function and display hotel details
show_available_hotels()
