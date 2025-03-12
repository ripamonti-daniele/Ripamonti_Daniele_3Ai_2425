from os import system
system("cls")

titoli = []

def crea_titolo(nuovo, l, msg = True):
    if msg:
        t = input("inserisci il titolo del libro: ").strip().capitalize()
    else:
        t = input().strip().capitalize()
    
    if nuovo:
        while t in l:
            print("titolo già presente")
            t = input("inserisci il titolo del libro: ").strip().capitalize()
    else:
        while t not in l:
            print("titolo non trovato")
            t = input("inserisci il titolo del libro: ").strip().capitalize()
    
    return t

def aggiungi(l):
    t = crea_titolo(True, l)
    
    l.append(t)  

def modifica(l):
    t = crea_titolo(False, l)
    
    ind = l.index(t)
    
    print("inserisci il nuovo titolo:")
    t = crea_titolo(True, l, False)
    
    l[ind] = t

def elimina(l):
    t = crea_titolo(False, l)
        
    l.remove(t)

def visualizza(l):
    l.sort()
    print("titoli salvati:")
    x = 1
    for i in l:
        print(f"{x}: {i}")
        x += 1

def cerca(l):
    t = input("inserisci il titolo del libro: ").strip().capitalize()
    
    if t in l:
        print(f"{t} è presente nella collezione")
        
    else:
        print(f"{t} non è presente nella collezione")
    

def carica(path, l):
    f = open(path, "r", encoding="utf-8")
    for r in f:
        r = r.strip("\n")
        l.append(r)
        
    f.close()
    print("dati caricati")

def salva(path, l):
    f = open(path, "w", encoding="utf-8")
    for i in l:
        f.write(i + "\n")
        
    f.close() 
    print("dati salvati")

def menu():
    print("inserisci 1 per aggiungere un titolo")
    print("inserisci 2 per modificare un titolo")
    print("inserisci 3 per eliminare un titolo")
    print("inserisci 4 per visualizzare i titoli")
    print("inserisci 5 per cercare un titolo")
    print("inserisci 6 per caricare i dati da un file")
    print("inserisci 7 per salvare i dati su un file")
    print("inserisci 0 per uscire")
    
    opzioni = ("0", "1", "2", "3", "4", "5", "6", "7")
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
            aggiungi(titoli)
        case 2:
            modifica(titoli)
        case 3:
            elimina(titoli)
        case 4:
            visualizza(titoli)
        case 5:
            cerca(titoli)
        case 6:
            carica("compiti\\ripamonti_14-3-25\\file_dati.txt", titoli)
        case 7:
            salva("compiti\\ripamonti_14-3-25\\file_dati.txt", titoli)
    print()