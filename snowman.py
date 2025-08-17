import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Snowman ASCII Art stages
STAGES = [
     # Stage 0: Full snowman
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1: Bottom part starts melting
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 2: Only the head remains
     """
      ___  
     /___\\ 
     (o o) 
     """,
     # Stage 3: Snowman completely melted
     """
      ___  
     /___\\ 
     """
]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    """Display the current snowman stage and the word with underscores for unguessed letters."""
    print(STAGES[mistakes])  # show current stage
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: " + display_word.strip())

def play_game():
    secret_word = get_random_word()
    guessed_letters = []  # letters the user has guessed
    mistakes = 0           # number of incorrect guesses

    print("Welcome to Snowman Meltdown!")
    
    # Show initial game state
    display_game_state(mistakes, secret_word, guessed_letters)

    # For now, just prompt once
    guess = input("Guess a letter: ").lower()
    guessed_letters.append(guess)  # add to guessed letters
    print("You guessed:", guess)

    # Show updated game state after the guess
    display_game_state(mistakes, secret_word, guessed_letters)

if __name__ == "__main__":
    play_game()
