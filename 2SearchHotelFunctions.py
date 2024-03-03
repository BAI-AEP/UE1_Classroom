# L1 2
# Sequential execution
# Function can be called only after definition
# Encapsulation or information hiding - implementation details are hidden
# scope of num_days



# Step 1: Define the details of an available Hotel (DB)
hotel_name = "Hotel Aria"
city = "Olten"
no_of_rooms = 10
stars = 4
is_available = True
price_per_night = 100.50

# scope of the variable num_days
#num_days = 1

# Step 2: Search Hotel

# Step 2.1: Define a function to set search criteria (with return)
def search_hotel():
    # set search criteria
    num_days = 5
    return num_days

#print(num_days)
# Step 2.2: Call the function and display search criteria
num_days = search_hotel()
print("User wants to stay for %d days" % num_days)


# Step 3: Show available hotels

# Step 3.1: Define a function to show hotel details (without return)
def show_hotels():
    print("Name: %s" % hotel_name)
    print("City: %s" % city)
    print("No. of rooms: %d" % no_of_rooms)
    print("Stars: %d" % stars)
    print("Price per night: %.2f" % price_per_night)
    print("Availability: %s" % is_available)


# Step 3.2: Call the function and display hotel details
show_hotels()


# Step 3.3: Define a function to calculate total price
def calculate_total_price():
    num_days = search_hotel()
    total_price = num_days * price_per_night
    print("Total price for %d days: %.2f" % (num_days, total_price))


# Step 3.4: Call the function and display hotel details
calculate_total_price()
