import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Enter your guess: "))

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts!")
            break

if __name__ == "__main__":
    guessing_game()
