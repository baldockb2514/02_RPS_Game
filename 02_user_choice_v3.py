# Version 3 - checks that response is in given list

# Functions go here
def choice_checker(question, valid_list, error):
    valid = False
    while not valid:

        # Ask user for choice and put it in lowercase
        response = input(question).lower()

        # iterates through list and if response is an item in the list (or the first letter in an item),
        # the full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

            else:
                print(error)
                print()


# Main routine goes here

# lists for checking purposes
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user for choice and check it's valid
user_choice = ""
while user_choice != "xxx":
    # Ask user for choice and check that it's valid
    user_choice = choice_checker("Please choose Rock / Paper / Scissors ", rps_list,
                                 "Please choose from rock / paper/ scissors (or xxx to quit)")

    # Print out choice for comparison purposes
    print(f"You chose {user_choice}")
    print()
