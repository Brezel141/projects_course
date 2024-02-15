import random


def run_game():

    word: str = random.choice(["apple", "banana", "carrot", "dog", "elephant", "flower",])

    name: str = input("What is your name? ")
    print(f"Hello, {name}! Welcome to Hangman!")

    # Setup
    guessed: str = ""
    tries: int = 5

    # Create a while loop
    while tries > 0:
        blanks: int = 0

        print('Word: ', end='')
        for char in word:
            if char in guessed:
                print(char, sep=', ', end='')
            else:
                print('_', end='')
                blanks += 1

        print()  # Adds a blank line

        if blanks == 0:
            print('You win!')
            break

        guess: str = input('Enter a letter: ')

        if guess in guessed:
            print(f'You already used: "{guessed}". Please try with another letter!')
            continue

        guessed += guess

        if guess not in word:
            tries -= 1
            print(f'Sorry, that was wrong... ({tries} tries remaining)')

            if tries == 0:
                print('No more tries remaining... You lose.')


if __name__ == '__main__':
    run_game()
