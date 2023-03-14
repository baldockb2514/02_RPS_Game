def check_rounds():
    while True:
        response = input("How many rounds?: ")

        round_error = "Please type either <enter> or an integer that is more than 0"

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


# Main routine goes here...

rounds_played = 0
choose_instruction = "Please choose rock (r), paper (p) or scissors (s)"

# Ask user for # of rounds, <enter for indefinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Rounds Heading
    print()
    if rounds == "":
        heading = f"Continuous Mode: Round {rounds_played}"
        print(heading)
        choose = input(f"{choose_instruction} or 'xxx' to end:")
        if choose == "xxx":
            break

    else:
        heading = f"Round of {rounds_played + 1} of {rounds}"
        print(heading)
        choose = input(choose_instruction)
        if rounds_played == rounds:
            break

    # rest of the loop / game
    print(f"You chose {choose}")

    rounds_played += 1

print("Thank you for playing")
