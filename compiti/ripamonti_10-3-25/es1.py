import modulo_ordinamento
from os import system
system("cls")

manga = {
    "Dragonball": ("Akira Toryiama", "Shūeisha", 42, True),
    "aaaaa": ("Akira Toryiama", "Shūeisha", 23, True),
    "cccc": ("Akira Toryiama", "Shūeisha", 11, False),
    "bbbbb": ("Akira Toryiama", "Shūeisha", 102, False),
    "One Piece": ("Eiichiro Oda", "Shūeisha", 109, False)
}

def chiedi_nome(messaggio, lmin = 0 , lmax = 30):
    n = input(messaggio).strip()
    while len(n) < lmin or len(n) > lmax:
        print(f"errore, lunghezza non valida (min {lmin} - max {lmax})")
        n = input(messaggio).strip()
        
    return n

def chiedi_volumi(chiedi_compl = True, msg = "\ninserisci il numero di volumi che costituiscono il manga: "):
    errore = True
    while errore:
        try:
            vol = int(input(msg))
        except:
            print("errore: devi inserire un numero intero")
            continue
        
        if vol < 1:
            print("errore: il manga deve essere costituito da almeno un volume")
        else:
            errore = False
    
    if not(chiedi_compl):
        return vol
    
    else:         
        compl = input("\ninserici 1 se il manga è completo, inserisci 0 se è incompleto: ").strip()
        while compl != "1" and compl != "0":
            compl = input("errore: inserici 1 se il manga è completo, inserisci 0 se è incompleto: ").strip()
            
        if compl == "1":
            compl = True
        elif compl == "0":
            compl = False
            
        return vol, compl 

def aggiungi_manga(manga):
    titolo = chiedi_nome("inserisci il nome del manga: ", 3)
    while titolo in manga:
        print("errore: il manga fa già parte della lista")
        titolo = chiedi_nome("\ninserisci il nome del manga: ", 3)
        
    autore = chiedi_nome("\ninserisci il nome dell'autore: ", 3, 20)
    casa_editrice = chiedi_nome("\ninserisci il nome della casa editrice: ", 3, 20)
    volumi, completo = chiedi_volumi()
    
    manga[titolo] = (autore, casa_editrice, volumi, completo)

def visualizza(manga, l = manga.keys()):
    x = 0
    for i in l:
        x += 1
        if manga[i][3] == False:
            msg = "Non completo"
        else:
            msg = "Completo"
        print(str(x) + ": " + i + "\n   Autore: " + manga[i][0] + " - Casa editrice: " + manga[i][1] + " - Volumi: " + str(manga[i][2]) + " - " + msg + "\n")

def chiedi_autore(manga):
    autori = set()
    for i in manga.keys():
        autori.add(manga[i][0])
        
    autore = chiedi_nome("inserisci il nome di un'autore: ", 3, 20)
    while autore not in autori:
        print("errore: autore non trovato")
        autore = chiedi_nome("inserisci il nome di un'autore: ", 3, 20)
        
    return autore

def visualizza_per_autore(manga):
    autore = chiedi_autore(manga)
    
    vol = [[], []]
    for i in manga.keys():
        if manga[i][0] == autore:
            if manga[i][3]:
                vol[0].append(manga[i][2])
            else:
                vol[1].append(manga[i][2])
                
    modulo_ordinamento.insertion_sort(vol[0], False)
    modulo_ordinamento.insertion_sort(vol[1], False)
    
    titoli = []
    for i in vol[0]:
        for j in manga.keys():
            if manga[j][0] == autore and manga[j][2] == i and manga[j][3]:
                titoli.append(j)
            if len(titoli) == len(vol[0]):
                break
            
    for i in vol[1]:
        for j in manga.keys():
            if manga[j][0] == autore and manga[j][2] == i and manga[j][3] == False:
                titoli.append(j)
            if len(titoli) == len(vol[1]) + len(vol[0]):
                break

    print(f"manga pubblicati da {autore}:")
    visualizza(manga, titoli)
    
def visualizza_per_volumi(manga):
    n = chiedi_volumi(False, "inserisci il numero minimo di volumi dei manga da visualizzare: ")
    
    titoli = []
            
    for i in manga.keys():
        if manga[i][2] >= n:
            titoli.append(i)
    
    print(f"i manga con almeno {n} volumi sono:")      
    visualizza(manga, titoli)
    
def visualizza_tot_manga(manga):
    autore = chiedi_autore(manga)
    
    mng = 0
    vol = 0
    
    for i in manga.keys():
        if manga[i][0] == autore:
            mng += 1
            vol += manga[i][2]
            
    print(f"{autore} ha pubblicato {mng} manga, per un totale di {vol} volumi")
    
def menu():
    print("inserisci 1 per aggiungere un manga alla collezione")
    print("inserisci 2 per visualizzare i manga")
    print("inserisci 3 per visualizzare i manga di un autore a tua scelta")
    print("inserisci 4 per visulizzare i manga costituiti da almeno x volumi (x a tua scelta)")
    print("inserisci 5 per visualizzare quanti manga e quanti volumi a pubblicato un autore a tua scelta")
    print("inserisci 0 per uscire")
    
    opzioni = ("1", "2", "3", "4", "5", "0")
    scelta = input().strip()
    while scelta not in opzioni:
        print("errore: scelta non valida")
        scelta = input().strip()
    
    print()
    
    return int(scelta)

scelta = -1

while scelta != 0:
    scelta = menu()
    match scelta:
        case 1:
            aggiungi_manga(manga)
        case 2:
            print("manga presenti nella collezione:")
            visualizza(manga)
        case 3:
            visualizza_per_autore(manga)
        case 4:
            visualizza_per_volumi(manga)
        case 5:
            visualizza_tot_manga(manga)
    print()