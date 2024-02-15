from random import randint

# Start the program with basic setup
lower_num, upper_num = 1, 10
random_number = randint(lower_num, upper_num)
print(f'Guess the number in the range from {lower_num} to {upper_num}.')

# Initialize the number of attempts
attempts = 3

# Run a loop for the game with a limited number of attempts
for _ in range(attempts):
    # Get the user guess
    try:
        user_guess = int(input('Guess: '))
    except ValueError as e:
        print('Please enter a valid number.')
        continue

    # Check the user guess
    if user_guess > random_number:
        print('The number is lower')
    elif user_guess < random_number:
        print('The number is higher')
    else:
        print('You guessed it!')
        break
else:
    print(f'Out of attempts. The correct number was {random_number}.')
