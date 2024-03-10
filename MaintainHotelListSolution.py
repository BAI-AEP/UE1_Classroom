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
    print("Showing all hotels...")
    for hotel in hotel_list:
        print(
            f"Hotel name: {hotel[0]}, City: {hotel[1]}, No. of rooms: {hotel[2]}, Stars: {hotel[3]}, Available: {hotel[4]}, Price per night: {hotel[5]}")

    print(f"There are {len(hotel_list)} hotels in the DB")


# Define a function to let admin enter the details of a new hotel
def accept_hotel_details():
    h_name = input("Enter the name of the new hotel: ")
    h_city = input("Enter the name of the city: ")
    h_rooms = int(input("Enter the no. of rooms: "))
    h_stars = int(input("Enter the no. of stars: "))
    h_avail = False
    if (input("Enter the availability (yes/no): ")).lower() in ("true", "yes", "available", "ya", "ja", "y"):
        h_avail = True
    h_price = float(input("Enter the price per night: "))
    hotel = (h_name, h_city, h_rooms, h_stars, h_avail, h_price)
    return hotel


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


# Define a function to search hotel tuples by hotel name and then remove from hotel_list
def remove_hotel_by_name(h_name):
    for hotel in hotel_list:
        # replace condition
        if h_name.lower() in hotel[0].lower():
            # if h_name == hotel[0]:
            hotel_list.remove(hotel)
            print(f"Removed {hotel}")
        else:
            print("Sorry, no hotel matching the given name was found.")


# End: Definition all variables and functions


# Start: Main script
show_all_hotels()

# add a new hotel
# new_hotel = ("Hotel Meilenstein", "Olten", 15, 4, True, 200.50)
# new_hotel = accept_hotel_details()
# add_hotel(new_hotel)
# show_all_hotels()

# delete a hotel by its position in hotel_list
# deleted_hotel = remove_hotel_by_index(-1)
# print(f"Removed hotel {deleted_hotel}")
# show_all_hotels()

# delete a hotel by its value (tuple)
# remove_hotel_by_value(hotel1)
# show_all_hotels()

# delete a hotel by its name
hotel_name = 'ARIA'
remove_hotel_by_name(hotel_name)


# End: Main script
