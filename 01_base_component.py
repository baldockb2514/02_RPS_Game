import random


# functions go here

# Add decoration to a statement
def statement_decorator(statement, decoration):
    # Make string with three characters
    sides = decoration * 5

    # add decoration to start and ent of statement
    statement = "{} {} {}".format(sides, statement, sides)
    print(statement)

    return ""


# checks user response is yes/no to a given question
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        response = response.replace(" ", "")

        if response == "yes" or response == "y":
            response = "yes"
            return response

            # If they say no, output 'display instructions'

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes / no")


# Displays instructions
def instructions():
    print("**** How to Play ****")
    print()
    print("Choose either a number of rounds or press <enter> for continuous mode")
    print()
    print("Then for each round, choose from Rock(r), Paper(p),\nScissors(s), or xxx to quit")
    print()
    print("Rock beats Scissors \nScissors beat Paper \nPaper beats Rock")
    print()
    print("!! Have Fun !!")
    print()
    return ""


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
            if response == item[0].lower() or response == item.lower():
                return item

        print(error)
        print()


# Main routine goes here

# Lists of valid responses
yes_no_list = ["yes", "no"]
rps_list = ["Rock", "Paper", "Scissors", "xxx"]

# Game title
print()
statement_decorator("Welcome to Rock, Paper, Scissors", "*")

# Ask user if they have played before
# If No, show instructions
print()
see_instructions = yes_no("Would you like to see the instructions? ")
print()
if see_instructions == "yes":
    instructions()

# Ask user for # of rounds then loop...
rounds_played = 0

# initialise lost / drawn counters
rounds_drawn = 0
rounds_lost = 0

# Ask user for # of rounds, <enter> for indefinite mode
rounds = check_rounds()

# Set up list for game stats
game_summary = []

# Ask user for choice and check that it's valid
global result
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
        result_decoration = "~"
    # win requirements + statements
    elif choose == "Rock" and comp_choice == "Scissors" or choose == "Paper" and comp_choice == "Rock" or \
            choose == "Scissors" and comp_choice == "Paper":
        result = "Won"
        result_decoration = "!"
    # End game if exit code is typed
    elif choose == "xxx":
        break
    # If nothing else applies, you lost
    else:
        result = "Lost"
        rounds_lost += 1
        result_decoration = "/"

    if result == "tie":
        round_result = "It's a tie"
    else:
        round_result = f"{choose} vs {comp_choice} - You {result}"

    outcome = "Round {}: {}".format(rounds_played + 1, result)

    game_summary.append(outcome)

    # rest of the loop / game
    # print results
    statement_decorator(round_result, result_decoration)

    rounds_played += 1

    # end game if requested # of rounds has been played
    if rounds_played == rounds:
        break

# Quick Calculations
rounds_won = rounds_played - rounds_drawn - rounds_lost

# Ask user if they want to see their game history
# If 'yes' show game history
if rounds_played + 1 >= 10:

    # Calculate game stats
    percent_win = rounds_won / rounds_played * 100
    percent_lost = rounds_lost / rounds_played * 100
    percent_drawn = rounds_drawn / rounds_played * 100

    print()
    print(statement_decorator("Game History", "*"))
    for game in game_summary:
        print(game)

    print()

    # displays game stats with % values to the nearest whole number
    print("******* Game Statistics *******")
    print("Win: {}, ({:.0f}%)\nLoss: {}, "
          "({:.0f}%)\nTie: {}, ({:.0f}%)".format(rounds_won, percent_win, rounds_lost, percent_lost,
                                                 rounds_drawn, percent_drawn))

else:
    # End of game statements
    print()
    print(statement_decorator("End Game Summary", "*"))
    print("Won: {} \t|\t Lost: {} \t|\t Drawn: {}".format(rounds_won, rounds_lost, rounds_drawn))

print()
print("Thanks for playing!")
