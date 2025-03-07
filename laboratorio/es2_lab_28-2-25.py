from os import system
from os import path
system("cls")

file = ["Ripamonti_Daniele_3Ai_2425\\laboratorio\\biblioteca\\testo1.txt",
        "Ripamonti_Daniele_3Ai_2425\\laboratorio\\biblioteca\\testo2.txt",
        "Ripamonti_Daniele_3Ai_2425\\laboratorio\\biblioteca\\testo3.txt",
        "Ripamonti_Daniele_3Ai_2425\\laboratorio\\biblioteca\\testo4.txt",
        "Ripamonti_Daniele_3Ai_2425\\laboratorio\\biblioteca\\testo5.txt",
        "Ripamonti_Daniele_3Ai_2425\\laboratorio\\biblioteca\\parolacce.txt"]

lett = ("abcdefghijklmnopqrstuvwxyz")

parole = {}
lettere = {}
parolacce = {"stupido": 0, "idiota": 0, "scemo": 0, "bastardo": 0}

for i in lett:
    lettere[i] = 0

for i in file:
    if path.exists(i):
        f = open(i, "r", encoding="utf-8")
        righe = f.read().lower()
        
        parole_testo = righe.split()
        for i in parole_testo:
            if i not in parole.keys():
                parole[i] = 1
            else:
                parole[i] += 1
                
            if i in parolacce.keys():
                parolacce[i] += 1
                
        for i in righe.replace(" ", "").replace("\n", ""):
            if i in lettere.keys():
                lettere[i] += 1
        
    else:
        print("errore nella ricerca dei file")

if len(parole) > 0:

    parole_50 = []
    x = 0

    while len(parole_50) < 50 and len(parole) > 0:
        for key, value in parole.items():
            if value >= x:
                x = value
                p = key
                
        parole_50.append(p)
        parole.pop(p)
        x = 0

    tot_lettere = 0
    for i in lettere.values():
        tot_lettere += i
    
    for key, value in lettere.items():
        lettere[key] = round(value / tot_lettere, 2)

    # messa a schermo
    print(f"{len(parole_50)} parole più utilizzate:")
    for i in range(len(parole_50)):
        print(i + 1, "-->", parole_50[i])
        
    print("\n---------------------------------\n")

    print("frequenze lettere:")
    for key, value in lettere.items():
        print(key, "-->", value)


    print("\n---------------------------------\n")

    print("parolacce:")
    for key, value in parolacce.items():
        print(key, "--> scritta", value, "volte")