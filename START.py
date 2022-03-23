import random
import os
from time import sleep
import copy
import asyncio

try:
    from rich.console import Console
    import keyboard
except:
    print("I tried to install this for you but it didn't run, so try running `pip install rich keyboard`")

terrainList = [0]
terrainMatrix = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]
check = 0
check2 = 0
playerMatrix = [[]]
xpos = 0
ypos = 0
fov = 10

width = 120

console = Console(width=width)

def terrainGen():
    global terrainList
    global terrainMatrix
    global playerMatrix
    global check
    global check2

    terrainList[0] = random.randint(1,2)

    for i in range(fov - 1):
        terrainList += " "
        terrainList[i+1] = terrainList[i] + random.randint(-1,1)
    check = max(terrainList)
    count = min(terrainList)

    if count < 1:
        check2 = check + abs(count) + 1
    else:
        check2 = check
    print("")

    terrainMatrix.append([])
    for j in range(check2):
        terrainMatrix.append([])
        for i in range(fov):
            if terrainList[i] >= check:
                terrainMatrix[j].append(0)
            else:
                terrainMatrix[j].append(" ")
        check -= 1

def draw():
    for j in range(check2):
            for i in range(fov):
                print(playerMatrix[j][i], end='')
            print("")

async def game():
    if keyboard.is_pressed("left") and xpos > 0 and terrainMatrix[ypos][xpos - 1] != 0:
        playerMatrix[ypos][xpos] = terrainMatrix[ypos][xpos]
        xpos -= 1
        playerMatrix[ypos][xpos] = 1
        os.system("cls")
        draw()
        sleep(.1)
            
    if keyboard.is_pressed("right") and xpos < fov and terrainMatrix[ypos][xpos + 1] != 0:
        playerMatrix[ypos][xpos] = terrainMatrix[ypos][xpos]
        xpos += 1
        playerMatrix[ypos][xpos] = 1
        os.system("cls")
        draw()
        sleep(.1)

    if keyboard.is_pressed("up") and ypos > 0:
        playerMatrix[ypos][xpos] = terrainMatrix[ypos][xpos]
        ypos -= 1
        playerMatrix[ypos][xpos] = 1
        os.system("cls")
        draw()
        sleep(.1)
    
    await asyncio.sleep(.5)
    if playerMatrix[ypos + 1][xpos] == " ":
        playerMatrix[ypos][xpos] = terrainMatrix[ypos][xpos]
        ypos += 1
        playerMatrix[ypos][xpos] = 1
        os.system("cls")
        draw()

terrainGen()
playerMatrix = copy.deepcopy(terrainMatrix)
print(len(terrainMatrix))
for i in range(len(terrainMatrix)):
    if terrainMatrix[i][0] == " ":
        ypos += 1
    else: break
ypos -= 1
playerMatrix[ypos][xpos] = 1

draw()
loop = asyncio.get_event_loop()
loop.run_until_complete(game())
loop.close()