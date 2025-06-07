import random


def get_word():
    words =  ["apple", "ball", "tree", "house", "elephant", "caterpillar", 
        "giraffe", "computer", "python", "keyboard", "javascript", "developer", "soccer", 
        "watermelon", "rocket", "champion", "library", "horizon", "starfish", "database", 
        "mountain", "exercise", "scenery", "wildlife", "adventure", "fireplace", "airplane", 
        "sunshine", "candle", "monitor", "camera", "planet", "universe", "dolphin", "butterfly",
        "jungle", "forest", "mountain", "island", "moon", "star", "planet", "solar", 
        "rainbow", "cloud", "stone", "iron", "sand", "wood", "rock", "earth",  "water", 
        "ocean", "desert", "oasis", "canyon", "cave", "horizon", "tornado", "volcano", "earthquake",
        "glacier", "hurricane", "blizzard", "snowstorm", "lightning", "tsunami", "cliff", "waterfall",
        "whirlpool", "fog", "mist", "breeze", "winds", "cyclone", "tornado", "earth", "soil", "mud", 
        "forest", "savannah", "rain", "storm", "thunder", "sunbeam", "sunlight", "shadow", "reflection", 
        "glow", "glimmer", "flash", "sparkle", "glitter", "shine", "twilight", "dawn", "dusk", "midnight", 
        "noon", "evening", "morning", "daylight", "sunrise", "sunset", "calm", "peace", "serenity", "joy",
        "harmony", "delight", "bliss", "laughter", "smile", "happiness", "freedom", "solace", "tranquility", 
        "elation", "contentment", "blissful", "ecstasy", "joyful", "cheerful", "optimism", "hope", "faith", 
        "trust", "belief", "strength", "resilience", "determination", "grit", "perseverance", "courage", 
        "bravery", "valor", "honor", "integrity", "loyalty", "respect", "kindness", "compassion", "generosity",
        "empathy", "gratitude", "thankful", "appreciation", "understanding", "patience", "humility", 
        "forgiveness", "caring", "helpful", "altruism", "benevolence", "goodness", "positivity", "energy",
        "enthusiasm", "motivation", "focus", "discipline", "organization", "productivity", "creativity", 
        "imagination", "innovation", "invention", "curiosity", "exploration", "discovery", "adventure", 
        "journey", "expedition", "voyage", "quest", "mission", "destination", "dream", "aspiration", 
        "goal", "success", "achievement", "accomplishment", "progress", "growth", "development", "improvement",
        "evolution", "transformation", "change", "adaptation", "resurgence", "renewal", "rebirth", "newness",
        "breakthrough", "recovery", "healing", "restoration", "revival", "rejuvenation", "hopeful", 
        "uplifting", "inspiration", "motivate", "drive", "determined", "focused", "hardworking", "dedication",
        "ambition", "success", "victory", "champion", "winner", "hero", "star", "genius", "leader", "pioneer"
    ]
    return random.choice(words).upper()


def display_hangman(incorrect_guesses):
    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
          -------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
          -------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
          -------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
          -------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
          -------
        """,
        """
           -----
           |   |
           O   |
          / | \  |
           /   |
               |
          -------
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
          -------
        """
    ]
    print(stages[incorrect_guesses])


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print(display.strip())
    return "_" not in display


def hangman_game():
    word_to_guess = get_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_attempts = 6

    print("Welcome to Hangman!")
    print(f"The word has {len(word_to_guess)} letters.")

    game_won = False

    while incorrect_guesses < max_attempts and not game_won:
        display_hangman(incorrect_guesses)
        display_word(word_to_guess, guessed_letters)

        print(f"\nGuessed letters: {', '.join(sorted(list(guessed_letters)))}")
        print(f"Attempts left: {max_attempts - incorrect_guesses}")

        try:
            guess = input("Guess a letter: ").upper().strip()

            if not guess.isalpha() or len(guess) != 1:
                print("Invalid input. Please enter a single letter.")
                continue

            if guess in guessed_letters:
                print(f"You already guessed '{guess}'. Try a different letter.")
                continue

            guessed_letters.add(guess)

            if guess in word_to_guess:
                print(f"Good guess! '{guess}' is in the word.")
            else:
                print(f"Sorry, '{guess}' is not in the word.")
                incorrect_guesses += 1

            current_display_status = ""
            for letter in word_to_guess:
                if letter in guessed_letters:
                    current_display_status += letter
                else:
                    current_display_status += "_"

            if "_" not in current_display_status:
                game_won = True

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    print("\n--- GAME OVER ---")
    display_hangman(incorrect_guesses)
    display_word(word_to_guess, guessed_letters)

    if game_won:
        print(f"\n********** CONGRATULATIONS! You guessed the word: {word_to_guess} **********")
    else:
        print(f"\nToo many incorrect guesses! The word was: {word_to_guess}")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman_game()
    else:
        print("Thanks for playing! Goodbye!")


if __name__ == "__main__":
    hangman_game()
