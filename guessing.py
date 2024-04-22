import random

def generate_secret_number():
    # Generate a random 4-digit number as the secret number
    return str(random.randint(1000, 9999))

def get_guess_from_player(player_name):
    # player to enter a guess
    while True:
        guess = input(f"{player_name}, enter your guess (4-digit number): ")
        if guess.isdigit() and len(guess) == 4:
            return guess
        else:
            print("Invalid input. Please enter a valid 4-digit number.")

def get_matching_digits(secret_number, guess):
   
    matching_digits = sum(1 for x, y in zip(secret_number, guess) if x == y)
    return matching_digits

def play_game():
    print("Welcome to the Number Guessing Game!")

    player1_secret_number = generate_secret_number()
    print("Player 1 has set the secret number.")

    player2_attempts = 0
    while True:
        player2_guess = get_guess_from_player("Player 2")
        player2_attempts += 1

        if player2_guess == player1_secret_number:
            print("Congratulations! Player 2 guessed the number correctly.")
            print(f"Player 2 took {player2_attempts} attempts.")
            break
        else:
            matching_digits = get_matching_digits(player1_secret_number, player2_guess)
            print(f"Player 2, you have {matching_digits} correct digits.")

    player2_secret_number = generate_secret_number()
    print("Player 2 has set the secret number.")

    player1_attempts = 0
    while True:
        player1_guess = get_guess_from_player("Player 1")
        player1_attempts += 1

        if player1_guess == player2_secret_number:
            print("Congratulations! Player 1 guessed the number correctly.")
            print(f"Player 1 took {player1_attempts} attempts.")
            break
        else:
            matching_digits = get_matching_digits(player2_secret_number, player1_guess)
            print(f"Player 1, you have {matching_digits} correct digits.")

    if player1_attempts < player2_attempts:
        print("Player 1 wins and is crowned Mastermind!")
    elif player2_attempts < player1_attempts:
        print("Player 2 wins and is crowned Mastermind!")
    else:
        print("It's a tie!")

# Start the game
play_game()
