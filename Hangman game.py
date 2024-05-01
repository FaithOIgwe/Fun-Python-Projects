import random

def choose_word():
    word_list = ["apple", "banana", "orange", "grape", "kiwi", "pineapple", "strawberry", "blueberry", "peach"]
    return random.choice(word_list)

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
    secret_word = choose_word()
    guessed_letters = []
    attempts_left = 6

    while True:
        print("\n" + display_word(secret_word, guessed_letters))
        print(f"Attempts left: {attempts_left}")
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        elif guess not in secret_word:
            print("Incorrect guess!")
            attempts_left -= 1
            if attempts_left == 0:
                print("Sorry, you've run out of attempts. The word was:", secret_word)
                break
        else:
            print("Correct guess!")

        guessed_letters.append(guess)

        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations! You guessed the word:", secret_word)
            break

hangman()
