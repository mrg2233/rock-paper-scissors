import random

def GetWinner(cc, pc):
    if cc - pc == -1:
        print("You win!")
    elif cc - pc == 1:
        print("You lose!")
    elif cc - pc == -2:
        print("You lose!")
    elif cc - pc == 2:
        print("You win!")
    elif cc - pc == 0:
        print("It's a tie!")

## 1 = Rock
## 2 = Paper
## 3 = Scissors
cc = random.randint(1,3)
pc = int(input("Rock(1), Paper(2), or Scissors(3)? "))
    
GetWinner(cc, pc)
print(f"Computer's choice: {cc}")
print(f"Your choice: {pc}")
