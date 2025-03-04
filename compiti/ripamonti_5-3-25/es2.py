from os import system
from termcolor import colored
from random import choice
system("cls")

file = open("Ripamonti_Daniele_3Ai_2425\\compiti\\ripamonti_5-3-25\\testo2.txt")

frutti = []

x = None
while x != "":
    x = file.readline().replace("\n", "")
    frutti.append(x)
    
frutti.pop() 

frutti = tuple(frutti)

colori = ("green", "red", "blue", "magenta", "cyan", "yellow", "white", "black")

for i in frutti:
    print(colored(i, choice(colori)))