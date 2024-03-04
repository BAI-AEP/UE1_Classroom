# L2 5
# Accept search criteria from the user
# Use input() function
# Rearrange all function definitions to the top and function calls in the main script

# Step 1: Create a fake DB for hotels
# Step 2: Search Hotel
# Step 3: Show available hotels
# Step 4: Show total price of stay

# Start: Definition all variables and functions
# Step 1.1: Define the details of a Hotel (DB)
hotel_name = "Hotel Aria"
city = "Olten"
no_of_rooms = 10
stars = 4
is_available = True
price_per_night = 100.50


# Step 2.1: Define a function to set multiple search criteria and return
def search_hotels():
    # Ask user to enter the values
    # num_of_days = input("Enter the no. of days for your stay: ")
    # min_price = input("Enter the min. price you are looking for: ")
    # max_price = input("Enter the max. price you are looking for: ")

    # Type cast to appropriate data type
    num_of_days = int(input("Enter the no. of days for your stay: "))
    min_price = float(input("Enter the min. price you are looking for: "))
    max_price = float(input("Enter the max. price you are looking for: "))
    return num_of_days, min_price, max_price


# Step 3.1: Define a function to show available hotel details
def show_hotels_by_price_range(min_price, max_price):
    # print(f"datatype for max_price: {type(max_price)}")
    # print(f"datatype for min_price: {type(min_price)}")
    # print(f"datatype for max_price: {type(price_per_night)}")
    if max_price >= price_per_night >= min_price:
        print("We found the following hotel(s) matching your search criteria:")
        print("Name: %s" % hotel_name)
        print("City: %s" % city)
        print("No. of rooms: %d" % no_of_rooms)
        print("Stars: %d" % stars)
        print("Price per night: %.2f" % price_per_night)
    else:
        print("Sorry, no hotels in the given price range exist at the moment :(")


# Step 4.1: Define a function to print total price based on the no. of days of stay
def show_total_price(num_days):
    total_price = num_days * price_per_night
    return total_price


# End: Definition all variables and functions


# Start: Main execution script
# Step 2.2: Call the function and collect the criteria in a variable
criteria = search_hotels()
print(f"The datatype of criteria is: {type(criteria)}")
print("Search criteria are: " + str(criteria))

# Step 3.2: Call the function and display hotel details
show_hotels_by_price_range(criteria[1], criteria[2])
print(show_total_price(criteria[0]))
# End: Main execution script
