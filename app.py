import random
import logo_art
def guess_the_number():
lower_bound = 1
upper_bound = 100
number_to_guess = random.randint(lower_bound, upper_bound)
print(logo_art.logo)
print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")
attempts = 0
while True:
try:
guess = int(input("Enter your guess: "))
attempts += 1
if guess < lower_bound or guess > upper_bound:
print(f"Please guess a number between {lower_bound} and {upper_bound}.")
continue
if guess < number_to_guess:
print("Too low! Try again.")
elif guess > number_to_guess:
print("Too high! Try again.")
else:
print(f"Congratulations! You've guessed the number {number_to_guess} in
{attempts} attempts.")
break
except ValueError:
print("Invalid input! Please enter a number.")
if __name__ == "__main__":
 guess_the_number()
