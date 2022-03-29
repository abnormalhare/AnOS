# SCP-6284: The infinite program

import keyboard
import os
import random
import time
import platform

score = 0
ltos = ""
ranList = []
play = ""
map = [
       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
       [0, 1, 1, 1, 0, 0, 0, 1, 1, 0],
       [0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
       [0, 1, 1, 1, 0, 0, 1, 0, 0, 0],
       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
      ]
game = 1
charX = 0
charY = 0
    
def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def drawMap():
    clear()
    global map
    global charX
    global charY
    printMap = " "
    for i in range(len(map[0])):
        printMap += "-"
    printMap += "\n"
    for i in range(len(map)):
        printMap += "|"
        for j in range(len(map[i])):
            if charX == j and charY == i:
                test =  "1"
            elif map[i][j] == 0:
                test = " "
            elif map[i][j] == 1:
                test = "0"
            printMap += test
        printMap += "|\n"
    printMap += " "
    for i in range(len(map[0])):
        printMap += "-"
    return printMap

def lose():
    print("Oh no! You lose.")
    print(f"Score: {score}")
    time.sleep(3)
    clear()
    start_game(1)

def gameCheck():
    global ltos
    if int(play) == ltos:
        clear()
        reset()
    else:
        lose()

def reset():
    global score
    global ltos
    global ranList
    ltos = ""
    ranList = []
    score += 1
    game()

def printCalcAdd(list):
    global ltos
    ltos = ""
    for i in range(len(list)):
        if i != len(list) - 1:
            ltos += str(list[i]) + " + "
        else:
            ltos += str(list[i])
    print(ltos)
    ltos = 0
    for i in range(len(list)):
        ltos += list[i]

def randset(num1, num2, amnt):
    global ranList
    for i in range(amnt):
        r = random.randint(num1, num2)
        ranList.append(r)
        

def game2():
    global charX
    global charY
    global map
    printMap = drawMap()
    print(printMap)
    x = 1
    while x == 1:
        if keyboard.is_pressed("down") and charY < len(map) - 1 and map[charY + 1][charX] != 1:
            charY += 1
            printMap = drawMap()
            print(printMap)
        elif keyboard.is_pressed("up") and charY > 0 and map[charY - 1][charX] != 1:
            charY -= 1
            printMap = drawMap()
            print(printMap)
        elif keyboard.is_pressed("right") and charX < len(map[charY]) - 1 and map[charY][charX + 1] != 1:
            charX += 1
            printMap = drawMap()
            print(printMap)
        elif keyboard.is_pressed("left") and charX > 0 and map[charY][charX - 1] != 1:
            charX -= 1
            printMap = drawMap()
            print(printMap)
        time.sleep(.3)
            
        

def start_game2():
    global map
    x = 1
    print("Welcome to Game 2!")
    print("How to play: Get to the end!")
    print("             Use the arrow keys")
    print("Would you like to play? (y/n)")
    while x == 1:
        if keyboard.is_pressed("y"):
            x = 0
            game2()
        elif keyboard.is_pressed("n"):
            print("ok")
            return

def results():
    global game
    print("Good Job! You beat the game!")
    print(f" Score: {score}")
    print(f" Lives left: {ltos}")
    print(f" Bonus: {ranList}")
    print("Press Enter to Continue")
    play = input()
    clear()
    print("Loading...")
    time.sleep(3)
    print("ERROR: UNASSIGNED VARIABLE")
    time.sleep(.5)
    print("ERROR: FUNCTION UNCLOSED")
    time.sleep(1)
    print("ERROR: UNASSIGNED VARIABLE")
    print("ERROR: INT CANNOT EQUAL STR")
    print("ERROR: ")
    time.sleep(.1)
    print("Password: 2083593")
    time.sleep(.2)
    print("ERROR: 'run.py': NETWORK REFUSED: Permssion denied.")
    print("ERROR: 'ver.py': NETWORK REFUSED: Permssion denied.")
    print("ERROR: 'help.py': NETWORK REFUSED: Permssion denied.")
    print("ERROR: 'tree.py': NETWORK REFUSED: Permssion denied.")
    print("ERROR: 'instmemz.py': NETWORK REFUSED: Permssion denied.")
    print("ERROR: 'del.py': NETWORK REFUSED: Permssion denied.")
    print("ERROR: 'reboot.py': NETWORK REFUSED: Permssion denied.")
    print("ERROR: 'checkos.py': NETWORK REFUSED: Permssion denied.")
    print("ERROR: 'amog.py': NETWORK REFUSED: Permssion denied.")
    print("ERROR: '.py': NETWORK REFUSED: Permssion denied.")
    print("ERROR: '.py': NETWORK REFUSED: Permssion denied.")
    print("ERROR: '.py': NETWORK REFUSED: Permssion denied.")
    print("ERROR: '.py': NETWORK REFUSED: Permssion denied.")
    print("ERROR: '.py': NETWORK REFUSED: Permssion denied.")
    print("ERROR: '.py': NETWORK REFUSED: Permssion denied.")
    print("ERROR: '.py': NETWORK REFUSED: Permssion denied.")
    print("ERROR: '.py': NETWORK REFUSED: Permssion denied.")
    print("ERROR: '.py': NETWORK REFUSED: Permssion denied.")
    print("TESTING PING...")
    time.sleep(5)
    print("NO INTERNET CONNECTION. REBOOTING...")
    time.sleep(2.5)
    print("ERROR: 'reboot.py': File not found")
    print("EMERGENCY MODE: BOOTING GAME2...")
    time.sleep(4)
    clear()
    game = 2
    start_game2()
    
def game():
    global score
    global ranList
    global ltos
    global play
    global game
    if score == 0:
        print("Add these 2 numbers!")
    if score >= 100:
        return
    elif score >= 50:
        randset(1*(score + 3), 5*(score + 4), 4)
    elif score >= 25:
        randset(1, 5*(score + 2), 3)
    else:
        randset(1, 5*(score + 1), 2)
    printCalcAdd(ranList)
    play = input()
    try:
        gameCheck()
    except:
        print("That's not a number!")
        lose()
        
    
    
def start_game(played):
    global ranList
    if played == 0:
        print("Welcome to: A Game")
        print("Would you like to play? (y/n)")
    else:
        print("Play Again? (y/n)")
    play = input()
    clear()
    if play == "y":
        ranList = []
        game()
    elif play == "n":
        print("ok!")
        opersys()
    else:
        start_game(played)

def run_game():
    start_game(0)
    results()

def passwd():
    print("Type in the password")
    play = input()
    if play == "2083593":
        results()
    else:
        run_game()
    
def opersys():
    print("An OS: Build 0006")
    print("(G)ame")
    print("(P)assword")
    x=0
    while x == 0:
        if keyboard.is_pressed("g"):
            x = 1
            run_game()
        elif keyboard.is_pressed("p")
            x = 1
            passwd()
    
opersys()