# Functions go here
def choice_checker(question):
    valid = False
    while not valid:

        error = "Please choose from rock / paper/ scissors (or xxx to quit)"

        # Ask user for choice and put it in lowercase
        response = input(question).lower()

        if response == "rock" or response == "r":
            return "Rock"

        elif response == "paper" or response == "p":
            return "Paper"

        elif response == "scissors" or response == "s":
            return "Scissors"

        # Check for exit code
        elif response == "xxx":
            return response

        else:
            print(error)


# Main routine goes here

# Ask user for choice and check it's valid
user_choice = ""
while user_choice != "xxx":

    # Ask user for choice and check that it's valid
    user_choice = choice_checker("Please choose Rock / Paper / Scissors ")

    # Print out choice for comparison purposes
    print(f"You chose {user_choice}")

# Print out choice for comparison purposes
