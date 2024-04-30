import random


def get_user_choice():
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    return user_choice


def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'paper' and computer_choice == 'rock') or \
            (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"


def print_scoreboard(scores):
    print("Scoreboard:")
    for player, score in scores.items():
        print(f"{player}: {score}")


def play_game():
    scores = {'User': 0, 'Computer': 0}

    for round in range(1, 11):
        print(f"\nRound {round}:")

        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose {user_choice}. Computer chose {computer_choice}.")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            scores['User'] += 1
        elif result == "Computer wins!":
            scores['Computer'] += 1

    print("\nGame over!")
    print_scoreboard(scores)

    if scores['User'] > scores['Computer']:
        print("You win the game!")
    elif scores['User'] < scores['Computer']:
        print("Computer wins the game!")
    else:
        print("It's a tie!")


if __name__ == "__main__":
    play_game()