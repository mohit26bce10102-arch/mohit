import random

# We store the winning rules in a dictionary to avoid long if/elif chains.
# The 'key' is the player's move, and the 'value' is the move it specifically beats.
WIN_RULES = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}

def show_how_to_play():
    """Prints a simple guide on how to play the game."""
    print("\n--- HOW TO PLAY ---")
    print("1. Choose to play a 'Best of 3' or 'Best of 5' match.")
    print("2. When prompted, type rock (r), paper (p), or scissors (s).")
    print("3. Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")
    print("4. Draws occur if both players pick the same move. Draws DO NOT count towards the match score.")
    print("5. First player to reach the required wins takes the match!")

def get_player_move():
    """
    Loops endlessly until the user inputs a valid move.
    Accepts full words or just the first letter in any capitalization.
    """
    while True:
        move = input("Your move (rock/paper/scissors or r/p/s): ").strip().lower()
        if move in ['rock', 'r']:
            return 'rock'
        elif move in ['paper', 'p']:
            return 'paper'
        elif move in ['scissors', 's']:
            return 'scissors'
        else:
            print("Invalid input. Please try again.")

def play_match(points_to_win):
    """
    Executes a single match based on the required points to win (e.g. 2 points for a Best of 3).
    Returns a string indicating the winner ('player' or 'computer').
    """
    player_score = 0
    computer_score = 0
    options = ['rock', 'paper', 'scissors']

    print("\nMATCH START! First to " + str(points_to_win) + " wins.")

    # The loop runs dynamically until somebody hits the win target
    while player_score < points_to_win and computer_score < points_to_win:
        player_move = get_player_move()
        # Randomly choose the computer's move from the list
        computer_move = random.choice(options)

        print("Computer chose: " + computer_move.title())

        # Logic determining the winner
        if player_move == computer_move:
            print("--> It's a DRAW! (Round not counted)")
        elif WIN_RULES[player_move] == computer_move:
            print("--> YOU WIN this round!")
            player_score += 1
        else:
            print("--> COMPUTER WINS this round!")
            computer_score += 1

        print("Score: Player " + str(player_score) + " - " + str(computer_score) + " Computer\n")

    # Announce the overall match winner safely
    if player_score == points_to_win:
        print("*** MATCH COMPLETE: YOU WIN THE SERIES! ***")
        return "player"
    else:
        print("*** MATCH COMPLETE: COMPUTER WINS THE SERIES! ***")
        return "computer"

def main():
    """
    The main looping menu keeping the program alive and tracking session statistics.
    """
    print("Welcome to Rock Paper Scissors!")

    # Global Session trackers
    matches_played = 0
    matches_won = 0
    matches_lost = 0

    while True:
        print("\n=== MAIN MENU ===")
        print("1. Play Game")
        print("2. How to Play")
        print("3. Quit")

        choice = input("Enter choice (1-3): ").strip()

        if choice == '1':
            print("\nSelect Format:")
            print("1. Best of 3 (First to 2)")
            print("2. Best of 5 (First to 3)")
            fmt = input("Choice (1/2): ").strip()

            # Simple error handling and routing
            if fmt == '1':
                points_needed = 2
            elif fmt == '2':
                points_needed = 3
            else:
                print("Invalid format. Canceling game.")
                continue

            winner = play_match(points_needed)

            # Update tracking variables
            matches_played += 1
            if winner == "player":
                matches_won += 1
            else:
                matches_lost += 1

            # Check if user wants to keep playing, otherwise loops back to menu
            again = input("Play another match? (y/n): ").strip().lower()
            if again == 'n':
                break

        elif choice == '2':
            show_how_to_play()

        elif choice == '3':
            break
        else:
            print("Invalid input. Please choose 1, 2, or 3.")

    # Application shutdown process - prints final session stats
    print("\n=== FINAL SESSION STATS ===")
    print("Matches Played: " + str(matches_played))
    print("Matches Won   : " + str(matches_won))
    print("Matches Lost  : " + str(matches_lost))

    if matches_played > 0:
        win_percent = (matches_won / matches_played) * 100
        print("Overall Win % : " + str(round(win_percent, 2)) + "%")

    print("Thanks for playing! Goodbye.")

# standard execution trigger
if __name__ == "__main__":
    main()