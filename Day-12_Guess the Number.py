# Day 12 Project Guess the Number

import random

print("Welcome to the Number Guessing Game!")


def play_game():

    attempts_left = 0
    difficulty = input("Choose a difficulty 'easy' or 'hard': ").lower()
    if difficulty.startswith('h'):
        attempts_left += 5
    else:
        attempts_left += 10

    print("\nI am thinking of a number between 1 and 100")

    # Number to guess
    number = random.randint(1, 100)

    while attempts_left != 0:

        print(f"You have {attempts_left} attempts remaining to guess the number.")

        guess = 'Invalid number'
        while not guess.isdigit():
            guess = input("\nMake a guess: ")
            if not guess.isdigit():
                print("Invalid Input :( Try again.")

        guess = int(guess)

        if guess > number and attempts_left != 0:
            attempts_left -= 1
            print("Too High!")
            guess = "Invalid"

        elif guess < number and attempts_left != 0:
            attempts_left -= 1
            print("Too Low!")
            guess = "Invalid"

        elif guess == number:
            print(f"You got it! The answer was {guess}")
            break

        if attempts_left == 0:
            print("You've run out of guesses. You lose.")

    play_again = input("Play again? y or n: ")

    if play_again == 'y':
        play_game()
    elif play_again == 'n':
        print("\nHave a nice day!")


play_game()
