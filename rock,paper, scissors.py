import random

def play_game():
    choices = ['rock', 'paper', 'scissors']

    player_choice = input("Choose rock, paper, or scissors: ").lower()
    while player_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        player_choice = input("Choose rock, paper, or scissors: ").lower()

    computer_choice = random.choice(choices)

    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")

def main():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
