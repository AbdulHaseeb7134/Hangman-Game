import random

# List of words for the game
word_list = ["python", "programming", "hangman", "developer", "artificial", "intelligence", "github", "data", "science", "machine"]

def choose_word():
    """Randomly choose a word from the word list."""
    return random.choice(word_list)

def display_progress(word, guessed_letters):
    """Display the current progress of the word with guessed letters."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    print("Welcome to Hangman!")
    print("Try to guess the word letter by letter.")
    
    # Choose a random word
    word = choose_word()
    guessed_letters = set()
    attempts = 6  # Number of wrong guesses allowed
    
    while attempts > 0:
        # Display the current progress
        print("\nWord:", display_progress(word, guessed_letters))
        print(f"Attempts left: {attempts}")
        print("Guessed letters:", " ".join(sorted(guessed_letters)) if guessed_letters else "None")
        
        # Ask the user for a letter
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"Good job! The letter '{guess}' is in the word.")
        else:
            print(f"Oops! The letter '{guess}' is not in the word.")
            attempts -= 1
        
        # Check if the user has guessed the whole word
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You've guessed the word:", word)
            break
    else:
        print("\nGame Over! You've run out of attempts.")
        print("The word was:", word)

# Run the game
if __name__ == "__main__":
    hangman()
