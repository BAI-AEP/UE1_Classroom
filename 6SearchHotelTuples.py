# L2 6
# Define attributes of hotel as immutable tuples
# Use indices to access the elements in a tuple
# Try to add an element in the tuple
# Try to access out of index element

# Step 1: Define fake DB with hotels as tuples
# Step 2: Skip search by criteria
# Step 3: Display all hotel details
# Step 4: Display all available hotels


# Start: Definition all variables and functions
# Step 1.1: Define Hotel tuples (DB)
# Order of values: hotel_name, city, no_of_rooms, stars, is_available, price_per_night
hotel1 = ("Hotel Aria", "Olten", 10, 4, True, 100.50)
hotel2 = ("Hotel Amaris", "Olten", 10, 3, False, 168.00)
hotel3 = ("Hotel Arte", "Olten", 10, 4, False, 205.50)
hotel4 = ("Hotel Oltnerhof", "Olten", 10, 3, True, 120.00)
hotel5 = ("Villa Weber", "Olten", 10, 0, True, 100.50)

# Step 2.1: Skip search criteria

# Step 3.1: Define a function to show all hotel details
def show_all_hotels():
    # print("Hotel name: %s, City: %s, No. of rooms: %d, Stars: %d, Available: %s, Price per night: %.2f" % hotel1)
    # print("Hotel name: %s, City: %s, No. of rooms: %d, Stars: %d, Available: %s, Price per night: %.2f" % hotel2)
    # print("Hotel name: %s, City: %s, No. of rooms: %d, Stars: %d, Available: %s, Price per night: %.2f" % hotel3)
    # print("Hotel name: %s, City: %s, No. of rooms: %d, Stars: %d, Available: %s, Price per night: %.2f" % hotel4)
    # print("Hotel name: %s, City: %s, No. of rooms: %d, Stars: %d, Available: %s, Price per night: %.2f" % hotel5)

    print(f"Hotel name: {hotel1[0]}, City: {hotel1[1]}, No. of rooms: {hotel1[2]}, Stars: {hotel1[3]}, Available: {hotel1[4]}, Price per night: {hotel1[5]}")
    print(f"Hotel name: {hotel2[-6]}, City: {hotel2[-5]}, No. of rooms: {hotel2[-4]}, Stars: {hotel2[-3]}, Available: {hotel2[-2]}, Price per night: {hotel2[-1]}")

# Step 3.3: Show available hotels
def show_available_hotels():
    print("\nAvailable hotels are: ")
    if hotel1[4]:
        print(hotel1)
    if hotel2[4]:
        print(hotel2)
    if hotel3[4]:
        print(hotel3)
    if hotel4[4]:
        print(hotel4)
    if hotel5[4]:
        print(hotel5)

    # for i in range(len(hotel1)):
    #     print(hotel1[i])
    #     i += 1

# Start: Main script
# Step 3.2: Call the function and display hotel details
show_all_hotels()
# Step 3.4: Call the function and display available hotels
show_available_hotels()
# End: Main script



