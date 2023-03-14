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

# initialise lost / drawn counters
rounds_drawn = 0
rounds_lost = 0

# Ask user for # of rounds, <enter> for indefinite mode
rounds = check_rounds()

# Ask user for choice and check that it's valid
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
    choose_instruction = "Please choose Rock / Paper / Scissors (or xxx to quit) "
    choose_error = "Please choose from rock / paper/ scissors (or xxx to quit) "

    # Ask user for choice and check that it's valid
    choose = choice_checker(choose_instruction, rps_list, choose_error)

    # get computer choice
    comp_choice = random.choice(rps_list[:-1])

    # compare choices
    # if the comp choice and user choice is the same it's a tie
    if comp_choice == choose:
        result = "tie"
        rounds_drawn += 1
    # win requirements + statements
    elif choose == "rock" and comp_choice == "scissors" or choose == "paper" and comp_choice == "rock" or \
            choose == "scissors" and comp_choice == "paper":
        result = "won"
    # End game if exit code is typed
    elif choose == "xxx":
        break
    # If nothing else applies, you lost
    else:
        result = "lost"
        rounds_lost += 1

    if result == "tie":
        round_result = "It's a tie"
    else:
        round_result = f"{choose} vs {comp_choice} - you {result}"

    # rest of the loop / game
    # print results
    print(round_result)

    rounds_played += 1

    # end game if requested # of rounds has been played
    if rounds_played == rounds:
        break

# Ask user if they want to see their game history
# If 'yes' show game history

# Quick Calculations
rounds_won = rounds_played - rounds_drawn - rounds_lost

# End of game statements
print()
print("***** End Game Summary *****")
print("Won: {} \t|\t Lost: {} \t|\t Drawn: {}".format(rounds_won, rounds_lost, rounds_drawn))
print()
print("Thanks for playing!")
