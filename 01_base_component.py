import random


# functions go here

# ask the user how many rounds they want to play and check if the answer is valid
def check_rounds():
    while True:
        response = input("How many rounds?: ")

        round_error = "Please type either <enter> or an integer that is more than 0\n"

        # If infinite mode not chosen, check response is an integer more than 0
        if response != "":
            try:
                response = int(response)

                # If response is too low, output error and go back to the start of the loop
                if response < 1:
                    print(round_error)
                    continue

            # If the response isn't an integer, output an error and restart the loop
            except ValueError:
                print(round_error)
                continue

        return response


# check if the users input is in a given list, output an error if not
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

# Lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]

# Ask user if they have played before
# If No, show instructions

# Ask user for # of rounds then loop...
rounds_played = 0

# Ask user for choice and check that it's valid
choose_instruction = choice_checker("Please choose Rock / Paper / Scissors ", rps_list,
                                    "Please choose from rock / paper/ scissors (or xxx to quit)")

# Ask user for # of rounds, <enter for indefinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start of gameplay loop

    # Rounds Heading
    print()
    if rounds == "":
        heading = f"Continuous Mode: Round {rounds_played + 1}"

    else:
        heading = f"Round of {rounds_played + 1} of {rounds}"

    print(heading)
    choose = input(f"{choose_instruction} or 'xxx' to end: ")

    # End game if exit code is typed
    if choose == "xxx":
        break

    # rest of the loop / game
    print(f"You chose {choose}")

    rounds_played += 1
