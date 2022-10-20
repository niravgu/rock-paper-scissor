#importing libraries
from random import randint
import time

#create list
x = ["rock","paper","scissor"]

#computer selection
comp = x[randint(0,2)]

player = False

#condition
while player == False :
    player = input("which do you choose ? rock,paper or scissor")
    if player == comp :
        print ('tie!')
    elif player == "rock" :
        if comp == "paper" :
            print ("computer chose",comp)
            time.sleep (2)
            print("you lose", comp ,"covers",player)
        else :
            print ("computer chose", comp)
            time.sleep(2)
            print ("you win!",player,"smashes",comp)
    elif player == "paper":
        if comp == "scissor":
            print("computr choses ",comp)
            time.sleep(2)
            print("you lose ",comp ,"cuts", player)
        else:
            print("computer chose", comp)
            time.sleep(2)
            print("you win!",player,"covers",comp)
    elif player == "scissor":
        if comp == "rock":
            print ("computer chose",comp)
            time.sleep(2)
            print("you lose ", comp ,"smashes",player)
        else:
            print("computer chose", comp)
            time.sleep(2)
            print ("you win!",player, "cuts",comp)
    elif player == "q":
        print("game over")
        break
    else:
        print("that's not a valid input.please try again!")
    player = False
    comp =x[randint(0,2)]

