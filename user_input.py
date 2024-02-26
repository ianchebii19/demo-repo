
def user_input():
    # Ask the user for their name and store it in the "name" variable
    name = input("What is your name? ")

    # Ask the user for their age and store it in the "age" variable
    age = input("How old are you? ")

    # Ask the user for their location and store it in the "location" variable
    location = input("Where do you live? ")

    # Print out a personalized message using the collected information
    print(f"Hello {name}, you are {age} years old and live in {location}.")

# Call the function to execute the code
user_input()