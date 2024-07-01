import random

# List of words and their corresponding hints
words_with_hints = [
    ("python", "A popular programming language."),
    ("hangman", "A classic word guessing game."),
    ("openai", "The organization behind ChatGPT."),
    ("computer", "An electronic device for storing and processing data."),
    ("artificial", "__ intelligence (AI)."),
]

# Hangman visual stages
hangman_stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

def get_word_and_hint():
    return random.choice(words_with_hints)

def display_hangman(tries):
    return hangman_stages[tries]

def play_game():
    word, hint = get_word_and_hint()
    word_letters = set(word)
    guessed_letters = set()
    tries = 0
    max_tries = len(hangman_stages) - 1

    print("Welcome to Hangman!")
    print("Hint:", hint)

    while tries < max_tries and len(word_letters) > 0:
        print(display_hangman(tries))
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
        
        word_display = [letter if letter in guessed_letters else '_' for letter in word]
        print("Word:", " ".join(word_display))
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_letters:
            guessed_letters.add(guess)
            word_letters.remove(guess)
            print(f"Good job! {guess} is in the word.")
        else:
            guessed_letters.add(guess)
            tries += 1
            print(f"Sorry, {guess} is not in the word.")
        
        print()

    if len(word_letters) == 0:
        print("Congratulations! You've guessed the word:", word)
    else:
        print(display_hangman(tries))
        print("Game over! The word was:", word)

if __name__ == "__main__":
    play_game()