# RPS component 6 - scoring system

# rounds won wil be calculated (total - draw - lost - won)
rounds_played = 0
rounds_drawn = 0
rounds_lost = 0

# results for testing purposes
test_results = ["won", "won", "loss", "loss", "tie"]

# Play Game
for item in test_results:
    rounds_played += 1

    # Generate computer choice

    result = item

    if result == "tie":
        result = "It's a tie."
        rounds_drawn += 1
    elif result == "loss":
        result = "You lost :( Better luck next time"
        rounds_lost += 1

# Quick Calculations
rounds_won = rounds_played - rounds_drawn - rounds_lost

# End of game statements
print()
print("***** End Game Summary *****")
print("Wom: {} \t|\t Lost: {} \t|\t Drawn: {}".format(rounds_won, rounds_lost, rounds_drawn))
print()
print("Thanks for playing!")
