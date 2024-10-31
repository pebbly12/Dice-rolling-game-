import random

# Function to allow dice rolling by player 
def roll_dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    return dice1, dice2 

def diplaye_result(player1,player2,player1_total,player2_total):
    print(f"\n\033[1mResult of this round\033[0m")
    print(f"{player1}'s total: {player1_total}")
    print(f"{player2}'s total: {player2_total}")

    if player1_total > player2_total:
        print(f"\n{player1} wins this round!")
        return player1
    elif player2_total > player1_total:
        print(f"\n{player2} wins this round!")
        return player2 
    else:
        print("\nIt's a tie! No winner this round")
        return None 

# Main loop
def game_loop():
    player1 = input("Enter Player1's name: ").strip()
    player2 = input("Enter Player2's name: ").strip()
    player1_win = 0
    player2_win = 0 
    round_number = 1

    while True:
        print(f"\n---Round {round_number}---")

        # Player One turn
        print(f"It's {player1}'s turn to roll the dice!")
        print("Press Enter to roll...")
        dice1,dice2= roll_dice()
        print("Rolling...")
        print(f"{player1} rolls {dice1} and {dice2}")
        player1_total = dice1 + dice2 
        print(f"{player1}'s total: {player1_total}")

        # Player Two turn
        print(f"\nNow it's {player2}'s turn to roll the dice!")
        print("Press Enter to roll..")
        dice1,dice2 = roll_dice()
        print("Rolling...")
        print(f"{player2} rolls {dice1} and {dice2}")
        player2_total = dice1 + dice2
        print(f"{player2}'s total: {player2_total}")

        # Check round winner 
        round_winner = diplaye_result(player1,player2,player1_total,player2_total)
        if round_winner == player1:
            player1_win += 1
        elif round_winner == player2:
            player2_win += 1

        print(f"\n\033[1mScores after {round_number} round\033[0m")
        print(f"{player1}: {player1_win} win")
        print(f"{player2}: {player2_win} win")

        # Ask users to play again 
        play_again = input("\nDo you want to play another round(yes or no): ").strip().lower()
        if play_again != "yes":
            break

        round_number += 1
    
    # Final scores after each round 
    print("Final Scores:")
    print(f"{player1}: {player1_win} win(s)")
    print(f"{player2}: {player2_win} wins(s)")

    # Check overall winner of the rounds 
    if player1_win > player2_win:
        print(f"{player1} is the overall winner")
    elif player1_win < player2_win:
        print(f"{player2} is the overall winner")
    else:
        print("It's a tie overall")

if __name__ == "__main__":
    game_loop()
