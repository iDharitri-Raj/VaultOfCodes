import random


def choose_word():
    words = ["python", "hangman", "programming",
             "computer", "gaming", "openai", "language"]
    return random.choice(words)


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


def hangman():
    print("Welcome to Hangman!")
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6  # You can adjust the number of allowed attempts

    while True:
        print("\n" + display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            elif guess in word_to_guess:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                print("Incorrect guess.")
                attempts -= 1
                print(f"Attempts left: {attempts}")
                if attempts == 0:
                    print("Sorry, you're out of attempts. The word was:",
                          word_to_guess)
                    break
            if set(guessed_letters) == set(word_to_guess):
                print("Congratulations! You guessed the word:", word_to_guess)
                break
        else:
            print("Invalid input. Please enter a single letter.")


if __name__ == "__main__":
    hangman()
