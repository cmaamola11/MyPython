'''Roll a pair of dice.Add the values of the roll.Ask the user to guess a number.Compare the user's guess to the total value.Determine the winner (user or computer).'''
from random import randint
from time import sleep
#total_roll = 0
def get_user_guess():
  guess = int(raw_input("Enter your guess: "))
  return guess
def roll_dice(number_of_sides):
  first_roll = randint(1,number_of_sides)
  second_roll = randint(1,number_of_sides)
  max_val = number_of_sides*2
  print max_val 
  guess = get_user_guess()
  if guess> max_val:
    print "Invalid Guess"
  else:
    print "Rolling..."
    sleep(2)
    print first_roll
    sleep(1)
    print second_roll
    sleep(1)
    total_roll = first_roll + second_roll
    print total_roll
    print "Result..."
    sleep(2)
    if guess == total_roll:
      print "You Won"
    else:
      print "You Lost"
      
  
roll_dice(6)  
