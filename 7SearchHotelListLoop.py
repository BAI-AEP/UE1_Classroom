# L2 7
# Define attributes of hotel as immutable tuples
# Define a list of hotels where tuples can be added or removed
# Introduce for and while loop

# Step 1: Define DB
# Hotel details as tuples
# DB as a list of hotel tuples
# Step 2: Skip search criteria
# Step 3: Show all hotels
# Step 4: Show available hotels

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


# Step 3.1: Define a function to show all hotel details
def show_all_hotels():
    for hotel in hotel_list:
        # print(item)
        print(f"Hotel name: {hotel[0]}, City: {hotel[1]}, No. of rooms: {hotel[2]}, Stars: {hotel[3]}, Available: {hotel[4]}, Price per night: {hotel[5]}")
    #print(hotel) # outside the loop

# Step 3.3: Use lists instead to show available hotels
def show_available_hotels():
    print("Showing available hotels...")
    for hotel in hotel_list:
        if hotel[4]:
            print(f"Hotel name: {hotel[0]}, City: {hotel[1]}, No. of rooms: {hotel[2]}, Stars: {hotel[3]}, Available: {hotel[4]}, Price per night: {hotel[5]}")

    # using while loop
    # i  = 0
    # while i in range(len(hotel_list)):
    #     if hotel_list[i][4]:
    #         # print(hotel)
    #         print(hotel_list[i][0] + "\t" + hotel_list[i][1] + "\t" + str(hotel_list[i][2]) + "\t" + str(hotel_list[i][3]) + "\t" + str(
    #             hotel_list[i][4]) + "\t" + str(hotel_list[i][5]))
    #     i = i + 1 # what happens when you forget this?
    #     # i += 1 # another way to increment by 1

    # Nested loops - we can use nested loops since we have a collection inside a collection
    # However, loops are more useful when all elements are similar
    # Our tuple has different elements - some string, some integer etc.
    # for hotel in hotel_list: # outer loop for list
    #     if hotel[4]:
    #         for item in hotel: #inner loop for tuple
    #             print(item)


# Start: Main script
# Step 3.2: Call the function and display hotel details
show_all_hotels()
print()

# Step 3.4: Call the function and display available hotels
show_available_hotels()

# Try changing hotel details
# hotel3[3] = 5 # error as tuples are immutable
# End: Main script

# Ooops! Tuples, obviously, are not the right choice to define hotel details! We would never be able to make changes!