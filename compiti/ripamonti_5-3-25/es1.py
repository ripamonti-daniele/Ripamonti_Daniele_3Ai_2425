from os import system
from funzioni.modulo_ricerca import ricerca_lineare_migliorata
system("cls")

file = open("Ripamonti_Daniele_3Ai_2425\compiti\\ripamonti_5-3-25\\testo1.txt")

strumenti = []

x = None
while x != "":
    x = file.readline().replace("\n", "")
    strumenti.append(x)
    
strumenti.pop() #elimina l'ultimo elemento che sarebbe ""

cerca = input("inserisci il nome di uno strumento: ")

if ricerca_lineare_migliorata(strumenti, cerca):
    print("strumento trovato")
else:
    print("strumento non trovato")