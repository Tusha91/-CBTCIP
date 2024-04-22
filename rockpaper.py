import random

def get_user_choice():
    # enter choice (rock, paper, or scissors)
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    # Generate a random choice for the computer 
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    # game rules
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 'rock':
        return "You win!" if computer_choice == 'scissors' else "Computer wins!"
    elif user_choice == 'paper':
        return "You win!" if computer_choice == 'rock' else "Computer wins!"
    elif user_choice == 'scissors':
        return "You win!" if computer_choice == 'paper' else "Computer wins!"

def play_game():
    print("Welcome to Rock-Paper-Scissors!")

    while True:
        # user choice
        user_choice = get_user_choice()

        # computer choice
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        # the winner
        result = determine_winner(user_choice, computer_choice)
        print(result)

        # play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Start the game
play_game()
