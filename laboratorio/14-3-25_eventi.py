# si vuole realizzare un programma che gestisce una serie di eventi 
# nome evento (non vuoto)
# luogo (deve esistere)
# data (dev'essere futura)
# età minima per partecipare
# durata evento

# crud
# inserisci
# modifica (solo data ed età minima)
# visualizza
# cancella

# implementare funzuioni utili a memorizzare e caricare l'archivio
# fare una ricerca di tutti gli eventi che si svolgono dalla data odierna in poi 
# visualizzare l'elenco ordinando per data crescente (a parità di data ordino\ per età minima decrescente)

from os import system
system("cls")
import datetime
from modulo_ordinamento import insertion_sort

eventi = {
    "Corsa campestre": ["Dalmine", datetime.datetime(2025, 3, 17).date(), 16, 3],
    "Torneo calcio": ["Osio sotto", datetime.datetime(2025, 3, 13).date(), 13, 2]
}

luoghi = []

f = open("laboratorio\\archivio_luoghi.txt", "r", encoding="utf-8")
for r in f:
    r = r.strip("\n")
    luoghi.append(r)
        
f.close()

def chiedi_nome(lista, nuovo, msg):
    nomi = []
    for i in lista:
        nomi.append(i)

    while True:
        nome = input(f"inserisci il {msg} dell'evento: ").strip().capitalize()
        if len(nome) < 1:
            print(f"errore: non puoi lascire vuoto il {msg}")
            continue

        if nuovo:
            if nome in nomi:
                print(f"errore: {msg} già presente")
            else:
                return nome

        else:
            if nome not in nomi:
                print(f"errore: {msg} non trovato")
            else:
                return nome

def chiedi_data():
    oggi = datetime.datetime.now()

    while True:
        d = input("inserisci la data dell'evento nel formato gg-mm-aaaa: ").strip()
        try:
            d = datetime.datetime(int(d[6:]), int(d[3:5]), int(d[:2]))
        except ValueError:
            print("errore: formato data non valido")
            continue

        if (d - oggi).days < - 1:
            print("errore: questa data è già passta")
        else:
            return d.date()

def chiedi_numero(msg, tipo = int, minimo = None, massimo = None):
    while True:
        n = input(msg + ": ").strip()
        try:
            n = tipo(n)
        except ValueError:
            print("errore: formato numero non valido")
            continue

        if minimo != None and n < minimo:
            print(f"errore: numero troppo piccolo (almeno {minimo})")
            continue

        if massimo != None and n > massimo:
            print(f"errore: numero troppo grande (massimo {massimo})")
            continue

        return n

def nuovo(eventi, luoghi):
    nome = chiedi_nome(eventi.keys(), True, "nome")
    luogo = chiedi_nome(luoghi, True, "luogo")
    data = chiedi_data()
    eta_min = chiedi_numero("inserisci l'età minima per partecipare", minimo = 5, massimo = 100)
    durata = chiedi_numero("inserisci la durata dell'evento (ore)", tipo = float, minimo = 0.5, massimo = 48)
    eventi[nome] = [luogo, data, eta_min, durata]

def modifica(eventi):
    nome = chiedi_nome(eventi.keys(), False, "nome")
    sclt = input("inserisci 1 per modificare la data\ninserisci 2 per modificare l'età minima\n").strip()
    opzioni = ("1", "2")
    while sclt not in opzioni:
        print("scelta non valida")
        sclt = input("inserisci 1 oppure 2: ")

    if sclt == "1":
        eventi[nome] = chiedi_data()
    elif sclt == "2":
        eta_min = chiedi_numero("inserisci l'età minima per partecipare", minimo = 5, massimo = 100)

def elimina(eventi):
    nome = chiedi_nome(eventi.keys(), False, "nome")
    del eventi[nome]

def visualizza(eventi, Futuri = False):
    ind = 0
    for i in eventi.keys():
        if Futuri:
            oggi = datetime.datetime.now()
            d = str(eventi[i][1])
            d = datetime.datetime(int(d[:4]), int(d[5:7]), int(d[8:]))
            if (d - oggi).days < - 1:
                continue

        ind += 1
        print(f"{ind} - nome evento: {i}")
        print(f"    luogo: {eventi[i][0]}")
        print(f"    data: {eventi[i][1]}")
        print(f"    età minima: {eventi[i][2]}")
        print(f"    durata: {eventi[i][3]}")

def visualizza_ordinata(eventi): # da finire
    l = []
    for i in eventi.keys():
        elementi = [i]
        for j in eventi[i]:
            elementi.append(j)
        l.append(elementi)

def carica(path):
    dati = {}
    f = open(path, "r", encoding="utf-8")
    for r in f:
        r = r.strip("\n")
        elementi = r.split("|")
        nome = elementi[0]
        elementi.remove(nome)
        for i in range(len(elementi)):
            if i == 1:
                elementi[i] = datetime.datetime(int(elementi[i][:4]), int(elementi[i][5:7]), int(elementi[i][8:])).date()
            elif i == 2:
                elementi[i] == int(elementi[i])
            elif i == 3:
                elementi[i] == float(elementi[i])
        dati[nome] = elementi
        
    f.close()
    print("dati caricati")
    return dati

def salva(path, eventi):
    f = open(path, "w", encoding="utf-8")
    for i in eventi.keys():
        riga = str(i) + "|"
        for j in eventi[i]:
            riga += str(j) + "|"

        f.write(riga + "\n")
        
    f.close() 
    print("dati salvati")

def menu():
    print("inserisci 1 per aggiungere un evento")
    print("inserisci 2 per modificare un evento")
    print("inserisci 3 per eliminare un evento")
    print("inserisci 4 per visualizzare tutti gli eventi")
    print("inserisci 5 per visualizzare gli eventi futuri")
    print("inserisci 6 per visualizzare gli eventi in ordine di data")
    print("inserisci 7 per caricare i dati da un file")
    print("inserisci 8 per salvare i dati su un file")
    print("inserisci 0 per uscire")
    
    opzioni = ("0", "1", "2", "3", "4", "5", "6", "7", "8")
    sclt = input().strip()
    while sclt not in opzioni:
        print("scelta non valida")
        sclt = input().strip()
    
    print()   
    return int(sclt)

sclt = -1
while sclt != 0:
    sclt = menu()
    match sclt:
        case 1:
            nuovo(eventi, luoghi)
        case 2:
            modifica(eventi)
        case 3:
            elimina(eventi)
        case 4:
            visualizza(eventi)
        case 5:
            visualizza(eventi, True)
        case 6:
            visualizza_ordinata(eventi)
            pass
        case 7:
            eventi = carica("laboratorio\\archivio_eventi.txt")
        case 8:
            salva("laboratorio\\archivio_eventi.txt", eventi)
    print()