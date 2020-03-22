from random import randint

player_wins = 0
computer_wins = 0

while player_wins < 2 and computer_wins < 2:
#User Selection
	print(f"Your Wins: {player_wins}")
	print(f"computer Wins: {computer_wins}")
	user_selection = input("Rock, Paper, Scissors -- ")

#Computer Selection

	computer_selection = None
	random_number = randint(1,3)

	if random_number == 1:
		computer_selection = "Rock"
	elif random_number == 2:
		computer_selection = "Paper"
	else:
		computer_selection = "Scissors"

#Comparisons 
	if user_selection == "Rock":
		if computer_selection == "Paper":
			print("YOU LOSE, PAPER COVERS ROCK")
			computer_wins += 1
		elif computer_selection == "Scissors":
			print("YOU WIN, ROCK BREAKS SCISSORS")
			player_wins += 1
		else:
			print("IT'S A TIE")
	elif user_selection == "Paper":
		if computer_selection == "Rock":
			print("YOU WIN, PAPER COVERS ROCK")
			player_wins += 1
		elif computer_selection == "Scissors":
			print("YOU LOSE, SCISSORS CUTS PAPER")
			computer_wins += 1
		else:
			print("IT'S A TIE")
	elif user_selection == "Scissors":
		if computer_selection == "PAPER":
			print("YOU WIN, SCISSORS CUTS PAPER")
			player_wins += 1
		elif computer_selection == "Rock": 
			print("YOU LOSE, ROCK BREAKS SCISSORS")
			computer_wins += 1
		else: 
			print("IT'S A TIE")