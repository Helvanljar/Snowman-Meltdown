import random
from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """
    Select and return a random word from the WORDS list.

    Returns:
        str: A randomly selected secret word.
    """
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """
    Display the current snowman stage and the secret word.

    Args:
        mistakes (int): Number of incorrect guesses made.
        secret_word (str): The word the player is trying to guess.
        guessed_letters (list): Letters that have already been guessed.
    """
    print(STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: " + display_word.strip())


def play_game():
    """
    Run a single session of Snowman Meltdown game.
    Handles guesses, mistakes, and win/loss conditions.
    """
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while True:
        print("\n" + "-" * 20)
        display_game_state(mistakes, secret_word, guessed_letters)
        print("-" * 20 + "\n")

        guess = input("Guess a letter: ").lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Good guess!")
        else:
            print("Wrong guess!")
            mistakes += 1

        # Check for win
        if all(letter in guessed_letters for letter in secret_word):
            print(
                f"Congratulations! You saved the snowman! "
                f"The word was '{secret_word}'."
            )
            break

        # Check for loss
        if mistakes >= max_mistakes:
            display_game_state(mistakes, secret_word, guessed_letters)
            print(
                f"Game over! The snowman melted. "
                f"The word was '{secret_word}'."
            )
            break


def main():
    """Run the game repeatedly until the player chooses to quit."""
    while True:
        play_game()
        replay = input("Do you want to play again? (y/n): ").lower()
        if replay != "y":
            print("Thanks for playing Snowman Meltdown!")
            break


if __name__ == "__main__":
    main()
