import random


def choose_word():
    words = ["python", "hangman", "challenge", "programming", "adventure"]
    return random.choice(words)


def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])


def play_hangman():
    print("Welcome to Hangman!")

    word_to_guess = choose_word()
    guessed_letters = set()
    attempts = 6

    while attempts > 0:
        print("\nWord to guess: " + display_word(word_to_guess, guessed_letters))
        print(f"Remaining attempts: {attempts}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in word_to_guess:
            guessed_letters.add(guess)
            print(f"Good job! {guess} is in the word.")
        else:
            attempts -= 1
            print(f"Sorry, {guess} is not in the word. You lose an attempt.")

        if all(letter in guessed_letters for letter in word_to_guess):
            print(f"\nCongratulations! You guessed the word: {word_to_guess}")
            break
    else:
        print(f"\nGame over! The word was: {word_to_guess}")


if __name__ == "__main__":
    play_hangman()
