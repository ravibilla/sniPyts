# Rock, paper, scissors
import random

player1 = ''
while player1 not in ["rock", "paper", "scissor"]:
    player1 = input("Enter Rock, Paper or Scissor: ").lower()

player2 = random.choice(["rock", "paper", "scissor"])

if player1 == "rock" and player2 == "paper":
    print("Paper beats Rock: Player 2 Won!")
elif player1 == "paper" and player2 == "scissor":
    print("Scissor beats Paper: Player 2 Won!")
elif player1 == "scissor" and player2 == "rock":
    print("Rock beats Scissor: Player 2 Won!")
elif player1 == player2:
    print("It's a Tie!")
else:
    print("Player 1 Won!")