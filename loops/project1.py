import random

random_number = random.randint(1,10)

#Handle User Guess

guess = None
#If They Guess Correctly, Tell them they won
while True:
	
	while guess != random_number:
		guess = input("Guess A Number Between 1 and 10 ---")
		guess = int(guess) 

		if guess == random_number:
			print("CONGRATS, YOU GOT IT")
			play_again = input("Do you want to Play again (Y/N)")

			if play_again == "Y":
				random_number = random.randint(1,10)
				guess = None

			else:
				print("Thank you For Playing")
				break

		elif guess < random_number:
			print("SORRY, TOO LOW - GUESS AGAIN")

		elif guess > random_number:
			print("SORRY, TOO HIGH - GUESS AGAIN")

		else: 
			print("Not a number, try again") 

#Let them Play Again if they want


