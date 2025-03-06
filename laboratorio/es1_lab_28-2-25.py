from os import system
system("cls")

lettere = "abcdefghiklmnopqrstvxyz"
modifica = "DEFGHIKLMNOPQRSTVXYZABC"

cifrario = {}
decodifica = {}

for i in range(len(lettere)):
    cifrario[lettere[i]] = modifica[i]
    decodifica[modifica[i]] = lettere[i]

import os
os.system("cls")

nome_file = input("inserisci il nome del file: ")
nome_file = "Ripamonti_Daniele_3Ai_2425\\laboratorio\\" + nome_file
if os.path.exists(nome_file):
    f = open(nome_file, "r", encoding="utf-8")
    righe = f.read()

    scelta = ""
    while scelta != "1" and scelta != "2":
        print("inserisci 1 per eseguire la codifica")
        print("inserisci 2 per eseguire la decodifica")
        scelta = input()
    
    codifica = ""
    
    if scelta == "1":
        if righe != righe.upper() and righe != righe.lower():
            righe = righe.lower()
            
        for x in righe:
            if x in cifrario.keys():
                codifica += cifrario[x]
            else:
                codifica += x
        
        codifica = codifica.upper()
        print("testo codificato")
                
    elif scelta == "2":
        if righe != righe.upper() and righe != righe.lower():
            righe = righe.upper()
            
        for x in righe:
            if x in decodifica.keys():
                codifica += decodifica[x]
            else:
                codifica += x

        codifica = codifica.lower()
        print("testo decodificato")
        
    f = open(nome_file, "w", encoding="utf-8")
    f.write(codifica)
    
    f = open(nome_file, "r", encoding="utf-8")
    x = f.read()
    
    f.close()

else:
    print("file non trovato")
