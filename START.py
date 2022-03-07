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
    for i in range(fov):
        terrainList += " "
        terrainList[i+1] = terrainList[i] + random.randint(-1,1)
    check = 1
    for i in range(fov):
        if check > terrainList[i]:
            check = terrainList[i]
    for j in range(abs(check)):
        if check < 0:
            for i in range(fov):
                terrainList[i] += abs(check)
    check = 0
    for i in range(fov):
        if check < terrainList[i]:
            check = terrainList[i]
    k = check
    for j in range(check):
        for i in range(fov):
            if terrainList[i] >= k:
                print(0, end='')
            else:
                print(" ", end='')
        print("\n")
        k -= 1

terrainGen()