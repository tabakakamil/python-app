from functions.name_checker import check_name

# Checking user's name from input
user_name = check_name(input("What's your name?\n"))
while not user_name:
    user_name = check_name(input("Try again, please.\n"))
