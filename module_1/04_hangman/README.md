# Hangman Game

This Python script is a simple implementation of the classic Hangman game. The script randomly selects a word, and the user has to guess the word one letter at a time.

## How It Works

At the start of the game, the script randomly selects a word from a predefined list. The user is then given 5 attempts to guess the word.

For each attempt, the user is prompted to enter a letter. If the letter is in the word, the script reveals its position(s) in the word. If the letter is not in the word, the user loses an attempt.

The game continues until the user guesses the word or runs out of attempts.

## Usage

Simply run the script, and enter your guesses when prompted. Enjoy the game!

## Example

```bash
What is your name? John
Hello, John! Welcome to Hangman!
Word: _ _ _ _ _
Enter a letter: a
Word: _ _ _ _ a
Enter a letter: e
Sorry, that was wrong... (4 tries remaining)
Word: _ _ _ _ a
Enter a letter: p
Word: a p p _ a
Enter a letter: l
Word: a p p l a
You win!