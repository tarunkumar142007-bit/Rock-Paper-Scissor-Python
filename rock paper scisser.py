
import time
from getpass import getpass
scoreA=0
scoreB=0


t=True
while t:
    n=input("Enter 'S' to Play 'X' to Quit: ").upper()
    print()
    l=["ROCK","PAPER","SCISSOR"]
    if n=='S':
        time.sleep(.5)
        PlayerA=getpass("Enter your choice for Player A: ").upper()
        PlayerB=getpass("Enter your choice for Player B: ").upper()
        if PlayerA not in l and PlayerB not in l:
            print("Both the player's made Invalid moves")
            scoreA+=-1
            scoreB+=-1
        elif PlayerA not in l:
            print("Player A made an Invalid move")
            scoreA+=-1
        elif PlayerB not in l:
            print("Player B made an Invalid move")
            scoreB+=-1
    
        if (PlayerA==PlayerB) or (PlayerA not in l and PlayerB not in l):
            print("Draw")
        elif (PlayerA == "ROCK" and PlayerB == "SCISSOR") or (PlayerA == "SCISSOR" and PlayerB == "PAPER") or (PlayerA == "PAPER" and PlayerB == "ROCK") or (PlayerB not in l):
            print("PlayerA wins this round")
            scoreA+=1
        else:
            print("PlayerB wins this round")
            scoreB+=1
        print()
        time.sleep(1)
    elif n=='X':
        t=False
        time.sleep(1)
        print()
    else:
        print("Only 'S' and 'X' are allowed!!!")
        time.sleep(1)

print('-----SCORES-----')
if scoreA<scoreB:
    time.sleep(.5)
    print(f"Total score of Player A is {scoreA}")
    print(f"Total score of Player B is {scoreB}")
    print()
    print("Player A loss")
    print("Player B won")
    print()
    print("Thank you for playing")
elif scoreB==scoreA:
    time.sleep(.5)
    print(f"Total score of Player A is {scoreA}")
    print(f"Total score of Player B is {scoreB}")
    print()
    print("Match Draw!")
    print()
    print("Thank you for playing")
else:
    time.sleep(.5)
    print(f"Total score of Player A is {scoreA}")
    print(f"Total score of Player B is {scoreB}")
    print()
    print("Player B loss")
    print("Player A won")
    print()
    print("Thank you for playing")