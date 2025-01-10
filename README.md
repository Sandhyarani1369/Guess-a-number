# Guess-a-number

# PROJECT NAME: 
# Guess the Number with Hints: * Write a number guessing game where
the computer gives hints like "too high" or "too low," and track the number of
attempts.*

#DISCRIPTION
# 1. Imports:
o The random module is imported to generate a random number for the game.
# 2. Game Logic (guess_the_number function):
# Introduction:
▪ Displays a welcome message and explains the game rules.
# Generate Random Number:
▪ Uses random.randint(1, 100) to select a random number between 1 and 100.
# Gameplay Loop:
▪ The game repeatedly asks the user for a guess until the correct number is
guessed:
# User Input:
▪ The program prompts the user to input a number.

▪ Input is validated to ensure it's an integer within the range of 1–100.

▪ Feedback:
▪ If the guess is too low, the user is informed with the message "Too low! Try
again."

▪ If the guess is too high, the message "Too high! Try again." is displayed.
# Success:
▪ When the correct number is guessed, the program congratulates the user and
displays the number of attempts taken.
# Error Handling:
▪ If the user enters invalid input (e.g., a non-numeric value), a ValueError is caught,
and the user is prompted to "Please enter a valid number."
# 3. Program Entry Point:
The if __name__ == "__main__": block ensures that the game runs only
when the script is executed directly, not when it is imported as a module
