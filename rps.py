import random

# CREATING A Rock Paper Scissors Game
# ------------------------
# ALL POSSIBLE COMBINATIONS

  #Rock = Rock
  #Rock < Paper
  #Rock > Scissors 

  #Paper > Rock
  #Paper = Paper
  #Paper < Scissors

  #Scissors < Rock
  #Scissors > Paper
  #Scissors = Scissors


user = input("What do you wanna play? ")
computerChoiceNumber = random.randint(1,3)
computerActualChoice = ""
if computerChoiceNumber == 1:
  computerActualChoice = "Rock"
elif computerChoiceNumber == 2:
  computerActualChoice = "Paper"
else:
  computerActualChoice = "Scissors"

  #User chooses Rock
  
print(computerActualChoice)

if user == "Rock" or user == "rock" and computerActualChoice == "Scissors":
  print("User Wins!")
elif user == "Rock" or user == "rock" and computerActualChoice == "Paper":
  print("User Losers!")
elif user == "Rock" or user == "rock" and computerActualChoice == "Rock":
  print("Tie!")

# User chooses Paper
  
elif user == "Paper" or user == "paper" and computerActualChoice == "Scissors":
  print("User Loses!")
elif user == "Paper" or user == "paper" and computerActualChoice == "Paper":
  print("Tie!")
elif user == "Paper" or user == "paper" and computerActualChoice == "Rock":
  print("User Wins!")

# User chooses Scissors

elif user == "Scissors" or user == "scissors" and computerActualChoice == "Scissors":
  print("Tie!")
elif user == "Scissors" or user == "scissors" and computerActualChoice == "Paper":
  print("User Wins!")
else:
  print("User Loses!")