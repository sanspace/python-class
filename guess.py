# Guess Your Number
import random

# Get a random Number
def get_random(min, max):
  """ returns a random number within the given range """
  return random.randrange(min, max + 1)

# Prompt User for a Number
def get_input(prompt):
  return int(input(prompt))

# Validate the Number
def validate_guess(guess, rand):
  """ return 0: Correct Guess, > 0 High Guess, < 0 Low Guess """
  if guess == rand:
    return 0
  else:
    return guess - rand

def game_master(tries):
  rand = get_random(1, 20)
  
  for i in range(1, tries + 1):
    guess = get_input("Enter your Guess: ")
    result = validate_guess(guess, rand)

    if result == 0:
      print("You win! The number is ", rand)
      print("Number of tries you've taken", i)
      exit() # Quit program
    elif result > 0:
      print("Your guess is high.")
      print("Please try again")
    elif result < 0:
      print("Your guess is low")
      print("Please try again")
  else:
    print("You've lost! The number is: ", rand)

game_master(3)

