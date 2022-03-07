from rich.console import Console
import random
import os

terrainList = [0]

width = 120
fov = 10

console = Console(width=width)

def terrainGen():
    global terrainList
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
    for j in range(check2):
        for i in range(fov):
            if terrainList[i] >= check:
                print(0, end='')
            else:
                print(" ", end='')
        print("")
        check -= 1

terrainGen()