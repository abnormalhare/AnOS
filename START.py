from rich.console import Console
import random
import os

terrainList = []

width = 120

console = Console(width=width)

def terrainGen():
    global terrainList
    terrainList[0] = random.randint(1,2)
    for i in range(10):
        terrainList[i+1] = terrainList[i] + random.randint(-1,1)
        