import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!")

    number_to_guess = random.randint(1, 100)
    number_of_attempts = 0

    while True:
        guess = input("Enter your guess: ")

        # Check if the input is a valid number
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        number_of_attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {number_of_attempts} attempts.")
            break

if __name__ == "__main__":
    guess_the_number()
