# L1 4
# Return single or multiple values from a function
# Introduce Tuple, index
# Tuples are immutable i.e., they cannot be modified
# Introduce scope of variables - global/local
# Introduce keyword "global"

# Step 1.1: Define the details of a Hotel (DB)
hotel_name = "Hotel Aria"
city = "Olten"
no_of_rooms = 10
stars = 4
is_available = True
price_per_night = 100.50


# Step 2: Search Hotel

# Step 2.1: Define a function to set multiple search criteria and return
def search_hotels():
    num_of_days = 5
    min_price = 50  # 120
    max_price = 150
    return num_of_days, min_price, max_price


# Step 2.2: Call the function and collect the criteria in a variable
# Step 2.3: criteria is a global variable which can be directly accessed inside any function
criteria = search_hotels()
print(type(criteria))
print("Search criteria are: " + str(criteria))


# Step 3: Show available hotels

# Step 3.1: Define a function to show available hotel details
def show_hotels_by_price_range():
    # why do we need to define min_price and max_price again? Can't reuse from search_hotel()?
    # note that criteria is accessing the global variable here
    min_price = criteria[1]
    max_price = criteria[2]

    # try min_price < price_per_night and max_price > price_per_night
    # simplify as a chained expression
    if max_price > price_per_night > min_price:
        print("Name: %s" % hotel_name)
        print("City: %s" % city)
        print("No. of rooms: %d" % no_of_rooms)
        print("Stars: %d" % stars)
        print("Price per night: %.2f" % price_per_night)
    else:
        print("Sorry, no hotels in the given price range exist at the moment :(")


# Step 3.2: Call the function and display hotel details
show_hotels_by_price_range()


# Step 3.3: Define function with parameters - criteria is a single parameter
# Avoid defining global variables and using/modifying inside a function
# Pass variable as input parameters and use return to collect results
# Code is easier to maintain and debug

def show_hotels_by_price_range(min_price, max_price):
    # now criteria is taken from the function argument and not from the global variable
    # here, both min_price and max_price are function parameters and have a local scope
    print(min_price, max_price)
    if min_price <= price_per_night <= max_price:
        print("Name: %s" % hotel_name)
        print("City: %s" % city)
        print("No. of rooms: %d" % no_of_rooms)
        print("Stars: %d" % stars)
        print("Price per night: %0.2f" % price_per_night)
        print("Availability: %s" % is_available)
    else:
        print("Sorry, no hotels in the given price range exist at the moment :(")


show_hotels_by_price_range(criteria[1], criteria[2])