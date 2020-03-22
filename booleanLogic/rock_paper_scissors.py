from random import randint

player_one_choice = input("Rock, Paper, Or Scissors")
random_Number = randint(1,3)
player_two_choice = None

if random_Number == 1:
	player_two_choice = "Rock"
elif random_Number == 2:
	player_two_choice = "Paper"
else:
	player_two_choice = "Scissors"


if (player_one_choice == "Rock") and (player_two_choice == "Rock"):
	print(f"Player One Chose {player_one_choice}")
	print(f"Player Two Chose {player_two_choice}")
	print("It's A Tie! Go Again")
elif(player_one_choice == "Rock") and (player_two_choice == "Paper"):
	print(f"Player One Chose {player_one_choice}")
	print(f"Player Two Chose {player_two_choice}")
	print("Player Two Wins")
elif(player_one_choice == "Rock") and (player_two_choice == "Scissors"):
	print(f"Player One Chose {player_one_choice}")
	print(f"Player Two Chose {player_two_choice}")
	print("Player One Wins")
elif (player_one_choice == "Paper") and (player_two_choice == "Rock"):
	print(f"Player One Chose {player_one_choice}")
	print(f"Player Two Chose {player_two_choice}")
	print("Player One Wins")
elif (player_one_choice == "Paper") and (player_two_choice == "Paper"):
	print(f"Player One Chose {player_one_choice}")
	print(f"Player Two Chose {player_two_choice}")
	print("It's a Tie! Go Again")
elif (player_one_choice == "Paper") and (player_two_choice == "Scissors"):
	print(f"Player One Chose {player_one_choice}")
	print(f"Player Two Chose {player_two_choice}")
	print("Player Two Wins!")
elif (player_one_choice == "Scissors") and (player_two_choice == "Rock"): 
	print(f"Player One Chose {player_one_choice}")
	print(f"Player Two Chose {player_two_choice}")
	print("Player Two Wins")
elif (player_one_choice == "Scissors") and (player_two_choice == "Paper"):
	print(f"Player One Chose {player_one_choice}")
	print(f"Player Two Chose {player_two_choice}")
	print("Player One Wins")
elif (player_one_choice == "Scissors") and (player_two_choice == "Scissors"): 
	print(f"Player One Chose {player_one_choice}")
	print(f"Player Two Chose {player_two_choice}")
	print("It's a Tie! Go Again")
else:
	print("Something Went Wrong")