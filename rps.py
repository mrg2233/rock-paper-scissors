import random

## Some basic stuff to get started.
tie = "Play again."
moves = ["ROCK", "PAPER", "SCISSORS"]
ranmov = random.choice(moves)
movin = input("Rock, Paper, or Scissors? Answer in ALL CAPS.")

## Now we know there is no tie.
if ranmov == "ROCK" and movin == "PAPER":
    print("You won! The AI guessed: " + ranmov)
elif ranmov == "PAPER" and movin == "SCISSORS":
    print("You won! The AI guessed: " + ranmov)
elif ranmov == "SCISSORS" and movin == "ROCK":
    print("You won! The AI guessed: " + ranmov)
elif ranmov == "ROCK" and movin == "SCISSORS":
    print("You lost! The AI guessed: " + ranmov)
elif ranmov == "PAPER" and movin == "ROCK":
    print("You lost! The AI guessed: " + ranmov)
elif ranmov == "SCISSORS" and movin == "PAPER":
    print("You lost! The AI guessed: " + ranmov)
## Is there a tie?
elif ranmov == movin:
    print(tie, "The AI also chose " + ranmov)

    
