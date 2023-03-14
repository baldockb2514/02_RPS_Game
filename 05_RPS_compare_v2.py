# Version 2 - make the code a bit more efficient
rps_list = ["rock", "paper", "scissors"]
comp_index = 0
for item in rps_list:
    user_index = 0
    user_choice = rps_list[user_index]
    comp_choice = rps_list[comp_index]
    user_index += 1
    # compare options

    # if the comp choice and user choice is the same it's a tie
    if comp_choice == user_choice:
        result = "It's a tie!"
    # win requirements + statements
    elif user_choice == "rock" and comp_choice == "scissors" or user_choice == "paper" and comp_choice == "rock" or \
            user_choice == "scissors" and comp_choice == "paper":
        result = "Congratulations! You Win!"
    # If nothing else applies, you lost
    else:
        result = "You lost :( Better luck next time"
    # print results
    print("You chose: {}"
          "\nComputer chose: {}."
          "\n{}".format(user_choice, comp_choice, result))

    comp_index += 1
    print()
