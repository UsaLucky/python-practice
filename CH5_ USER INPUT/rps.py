import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK =1
    PAPER =2
    SCISSORS =3

# print(RPS(2))
# print(RPS.ROCK)
# print(RPS['ROCK'])
# print(RPS.ROCK.value)
# sys.exit()

print("")
playerchoice = input("Enter.. \n 1 for Rock \n 2 for Paper, or \n 3 for Scissors:\n\n")

player = int(playerchoice)

if player < 1 or player >3:
    sys.exit("You must enter 1,2, or 3")

computerchoice = random.choice("123")

computer = int(computerchoice)

print("")
print("You Chose " + str(RPS(player)).replace('RPS.','') + ".")
# The method replace is used when you want to replace a specific part of an output
print("Python Chose " + str(RPS(computer)).replace('RPS.','')+ ".")
print("")

if player ==1 and computer ==3:
    print("🎉 you win!".title())
elif player ==2 and computer ==1:
    print("🎉 you win!".title())
elif player ==3 and computer ==2:
    print("🎉 you win!".title())
elif player == computer:
    print("😲 Tie game".title())
else: 
    print("🐍 You Lose")
