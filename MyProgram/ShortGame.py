from random import randint

guesses_left = 3
# Start your game!
while guesses_left > 0:
  random_number = randint(1, 10)
  guess = int(raw_input("Your guess: "))
  print random_number
  if guess == random_number:
    print "You win!"
    break
  guesses_left -=1
else:
  print "You lose."
