import os
from random import *
import monsters

def Encounter(PlayerHP, PlayerDMG, PlayerArmor, PlayerSlot1, PlayerSlot2, PlayerSlot3, PlayerSlot4, PlayerSlot5, Level):
    gamestate = {
        1 : 1,
        2 : 1
    }
    while(gamestate[1] == 1):
        encounter = getattr(monsters, "m"+str(randint(1,2)))        
        gamestate[2] = 1        
        print("You encounter a "+ str(encounter["name"]) + " !")
        print("Health: "+str(encounter["health"]))
        while(gamestate[2] == 1):
            print("WHAT WILL YOU DO?:")
            print("1. ATTACK / 2. FLEE / 3. ITEM" + os.linesep)
            option = input(">>> ")
            if ((option=="1") or (option=="2") or (option=="3")):
                if(option == "1"):
                    gamestate, encounter = EncounterAttack(PlayerDMG, **encounter)
                if(option == "2"):
                    print("you tried to flee")
                if(option == "3"):
                    print("you tried to use an item")
            else:
                print("Invalid input")

def EncounterAttack(DMGvar, **encountdict):
    roll = randint(1, 10)
    if(roll > int(encountdict["armor"])):
        print("A successful strike! You deal "+str(DMGvar)+" damage to the "+encountdict["name"])
        encountdict["health"] = (int(encountdict["health"]) - DMGvar)
        if(encountdict["health"] <= 0):
            print("The creature dies!")
            print("1. SAVE / 2. CONTINUE" + os.linesep)
            encounterfinish = input(">>>  ")
            if((encounterfinish=="1") or (encounterfinish=="2")):
                if(encounterfinish=="1"):
                    print("Name of your savegame" + os.linesep)
                    gametosave = input(">>>  ")
                    print("Password for your savegame" + os.linesep)
                    passtosave = input(">>>  ")
                    gamest = {
                        1 : 0,
                        2 : 0
                    }
                    return gamest, encountdict
                if(encounterfinish=="2"):
                    gamest = {
                        1 : 1,
                        2 : 0
                    }    
                    return gamest, encountdict
            else:
                 print("Invalid input" + os.linesep)
        else:
            gamest = {
            1 : 1,
            2 : 1
        }
        return gamest, encountdict
    else:
        print("The "+encountdict["name"]+"'s armor blocks the attack")
        gamest = {
            1 : 1,
            2 : 1
        }
        return gamest, encountdict
