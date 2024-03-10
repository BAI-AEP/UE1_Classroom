# US: As an admin, I want to maintain hotel details so that the data is up-to-date.
# maintain hotel list - add/remove hotels

# Start: Definition all variables and functions
# Step 1.1: Define Hotel tuples (DB)
# Order of values: hotel_name, city, no_of_rooms, stars, is_available, price_per_night
hotel1 = ("Hotel Aria", "Olten", 10, 4, True, 100.50)
hotel2 = ("Hotel Amaris", "Olten", 10, 3, False, 168.00)
hotel3 = ("Hotel Arte", "Olten", 10, 4, False, 205.50)
hotel4 = ("Hotel Oltnerhof", "Olten", 10, 3, True, 120.00)
hotel5 = ("Villa Weber", "Olten", 10, 0, True, 100.50)

# Step 1.2: Define a collection of hotels - List
hotel_list = [hotel1, hotel2, hotel3, hotel4, hotel5]


# Define a function to show all hotel details
def show_all_hotels():
    for hotel in hotel_list:
        print(
            f"Hotel name: {hotel[0]}, City: {hotel[1]}, No. of rooms: {hotel[2]}, Stars: {hotel[3]}, Available: {hotel[4]}, Price per night: {hotel[5]}")


def add_hotel():
    pass


def remove_hotel():
    pass

# End: Definition all variables and functions


# Start: Main script


# End: Main script
