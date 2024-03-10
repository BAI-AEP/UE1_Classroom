# US: As an admin, I want to maintain hotel details so that the data is up-to-date.
# maintain hotel details - name, city, rooms, stars, availability, price

# Start: Definition all variables and functions
# Step 1.1: Define Hotels as list (DB)
# Order of values: hotel_name, city, no_of_rooms, stars, is_available, price_per_night
hotel1 = {"hotel_name": "Hotel Aria", "city": "Olten", "no_of_rooms": 10, "stars": 4, "is_available": True,
          "price_per_night": 100.50}
hotel2 = {"hotel_name": "Hotel Amaris", "city": "Olten", "no_of_rooms": 10, "stars": 3, "is_available": False,
          "price_per_night": 168.00}
hotel3 = {"hotel_name": "Hotel Arte", "city": "Olten", "no_of_rooms": 10, "stars": 4, "is_available": False,
          "price_per_night": 205.50}
hotel4 = {"hotel_name": "Hotel Oltnerhof", "city": "Olten", "no_of_rooms": 10, "stars": 3, "is_available": True,
          "price_per_night": 120.00}
hotel5 = {"hotel_name": "Villa Weber", "city": "Olten", "no_of_rooms": 10, "stars": 0, "is_available": True,
          "price_per_night": 100.50}

# Step 1.2: Define a collection of hotels - List
hotel_list = [hotel1, hotel2, hotel3, hotel4, hotel5]


# Define a function to show all hotel details
def show_all_hotels():
    for hotel in hotel_list:
        print(
            f"Hotel name: {hotel["hotel_name"]}, City: {hotel["city"]}, No. of rooms: {hotel["no_of_rooms"]}, Stars: {hotel["stars"]}, Available: {hotel["is_available"]}, Price per night: {hotel["price_per_night"]}")


def add_hotel():
    pass


def remove_hotel():
    pass

# End: Definition all variables and functions


# Start: Main script


# End: Main script
