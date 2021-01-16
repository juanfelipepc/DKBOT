#Code to handle the game
#Relies on the socket already being started
import random

import game

while(1):
    print("    MAIN MENU")
    print("1. NEW GAME / " + "2. LOAD GAME / ")
    option = input(">>>  ")
    if((option=="1")or(option=="2")):
        if(option == "1"):
            game.Encounter(10,5,3,"","","","","",1)
        if(option == "2"):
            print("Name of your saved game?")
            savegame = input(">>>  ")
            print("Saved game password?")
            savedpass = input(">>> ")
    else:
        print("Invalid option")
        
    

    


##to-do:
##    make the saving to player file code
##    rest ofthe encounter options (flee, item)
##    load player stats from "load "game" options
##    more monsters
##    make items
##    item interactions with player stats
##    give option to use items after encounter
