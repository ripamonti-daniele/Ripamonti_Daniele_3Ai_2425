from os import system
system("cls")
from modulo_ordinamento import insertion_sort

strumenti = {}

def chiedi_nome(msg):
    while True:
        nome = input(f"inserisci nome {msg}: ").strip().capitalize()
        if len(nome) < 1:
            print(f"errore: non puoi lascire vuoto il nome")
        else:
            return nome
        
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
    
def nuovo(d):
    n = chiedi_nome("strumento")
    marca = chiedi_nome("marca")
    modello = chiedi_nome("modello")
    pezzi = chiedi_numero("inserisci il numero di pezzi", minimo = 1, massimo = 100)
    
    if (n, marca, modello) in d.keys():
        d[(n, marca, modello)] += pezzi
    else:
        d[(n, marca, modello)] = pezzi
        
def elimina(d):
    n = chiedi_nome("strumento")
    marca = chiedi_nome("marca")
    modello = chiedi_nome("modello")
    if (n, marca, modello) in d.keys():
        del d[(n, marca, modello)]
        errore = False
    else:
        print("errore: strumento non trovato")
    
def visualizza_modelli(d):
    n = chiedi_nome("strumento")
    marca = chiedi_nome("marca")
    
    modelli = []
    
    for i in d.keys():
        if i[0] == n and i[1] == marca:
            modelli.append((d[i[0], i[1], i[2]], i[2]))
            
    if len(modelli) == 0:
        print(f"nessun modello di {n} {marca} trovato")
        
    else:
        insertion_sort(modelli, False)
        print("modelli trovati:")
        for i in modelli:
            print("-", i[1], "-->", i[0], "pezzi")
            
def vendi(d):
    n = chiedi_nome("strumento")
    marca = chiedi_nome("marca")
    modello = chiedi_nome("modello")
    if (n, marca, modello) in d.keys():
        d[(n, marca, modello)] -= 1
        if d[(n, marca, modello)] == 0:
            del d[(n, marca, modello)]
    else:
        print("errore: strumento non disponibile")
            
def carica(path):
    avanti = False
    try:
        f = open(path, "r", encoding="utf-8")
        avanti = True
    except FileNotFoundError:
        print("file non trovato")
        
    if avanti:
        d = {}
        for r in f:
            r = r.replace("\n", "")
            dati = r.split("|")
            try:
                d[(dati[0], dati[1], dati[2])] = int(dati[3])
            except ValueError:
                print("errore: dati salvati in ordine inadeguato")
                
        print("dati caricati")
        return d
        
def salva(path, d):
    avanti = False
    try:
        f = open(path, "w", encoding="utf-8")
        avanti = True
    except FileNotFoundError:
        print("file non trovato")
    
    if avanti:
        for i in d.keys():
            for j in i:
                f.write(j + "|")
            f.write(str(d[i]) + "\n")
        print("dati salvati")

def menu():
    print("inserisci 1 per creare uno strumento o aggiungere dei pezzi")
    print("inserisci 2 per eliminare uno strumento")
    print("inserisci 3 per visualizzare un modello di strumento in base alla marca")
    print("inserisci 4 per vendere uno strumento")
    print("inserisci 5 per caricare i dati da un file")
    print("inserisci 6 per salvare i dati su un file")
    print("inserisci 0 per uscire")
    
    opzioni = ("0", "1", "2", "3", "4", "5", "6")
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
            nuovo(strumenti)
        case 2:
            elimina(strumenti)
        case 3:
            visualizza_modelli(strumenti)
        case 4:
            vendi(strumenti)
        case 5:
            strumenti = carica("compiti\\ripamonti_17-3-25\\dati.txt")
        case 6:
            salva("compiti\\ripamonti_17-3-25\\dati.txt", strumenti)
            
    print()