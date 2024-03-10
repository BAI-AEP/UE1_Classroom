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


# Define a function to add a new hotel to the list
def add_hotel(hotel):
    # hotel_list.append(new_hotel)
    hotel_list.insert(10, hotel)


# Delete a hotel from hotel_list
def remove_hotel_by_index(index):
    print(f"Removing hotel at position {index}...")
    hotel = hotel_list.pop(index)
    return hotel


# Define a function to remove hotel tuples from hotel_list
def remove_hotel_by_value(hotel):
    hotel_list.remove(hotel)
    print(f"Removed hotel {hotel}")


def edit_hotel(hotel, key, val):
    hotel[key] = val
    print(f"Updated hotel details: {hotel}")


# End: Definition all variables and functions


# Start: Main script
# add a new hotel
# new_hotel = {"hotel_name": "Hotel Meilenstein", "city": "Olten", "no_of_rooms": 15, "stars": 4, "is_available": True,
#              "price_per_night": 200.50}
# add_hotel(new_hotel)
# show_all_hotels()

# delete a hotel by its position in hotel_list
# deleted_hotel = remove_hotel_by_index(-1)
# print(f"Removed hotel {deleted_hotel}")
# show_all_hotels()

# edit details of a hotel by its key
edit_hotel(hotel1, "hotel_name", "Aparthotel Aria")

edit_hotel(hotel2, "is_available", True)
# End: Main script
