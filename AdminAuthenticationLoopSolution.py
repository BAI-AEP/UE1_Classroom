# US: As an admin, I want to log in so that I can perform actions authorized for my role.

# Step 1: Define admin login credentials
# Step 2: Enter username password, allow 3 unsuccessful attempts
# Step 3: Check if login successful or not

# Start: Definition all variables and functions
admin_username = "admin"  # valid username
admin_password = "admin"  # valid password
is_logged = False  # default login status
# End: Definition all variables and functions


# Start: Main script

attempt = 0
while not is_logged:
    username = input("Username: ")
    password = input("Password: ")
    if username == admin_username:
        if password == admin_password:
            is_logged = True

    if is_logged:
        print(f"You have been successfully logged in, welcome!")
    else:
        print(f"Sorry, authentication failed!")
        attempt = attempt + 1

    if attempt == 3:
        print(f"You exceeded your attempts to log in!")
        break
# End: Main script
