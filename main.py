#                                                                           Stone-Paper-Scissor



import random


def Game(com, player):
    if com == player:
        return None
    elif com == "s":
        if player == "p":
            return True
        elif player == "si":
            return False
    elif com == "p":
        if player == "s":
            return False
        elif player == "si":
            return True
    elif com == "si":
        if player == "s":
            return True
        elif player == "si":
            return False

print ("Computer's Turn : Stone(S) Paper(P) Scissor(Si) ")
randNo = random.randint(1,3)
if randNo == 1:
    com = "s"
elif randNo == 2:
    com = "p"
elif randNo == 3:
    com = "si"

player = input("Your Turn : Stone(S) Paper(P) Scissor(Si) ")
a = Game(com, player)

print(f"Computer's Choice : {com}")
print(f"Player's Choice : {player}")

if a == None:
    print("It's a Tie")
elif a:
    print("Congratulations, You Won!!!")
else:
    print("Sorry, You Lose!!!")