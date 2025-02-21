# Realizzare un programma nella quale l'utente può eseguire queste operazioni:
# 1) creare una nuova spedizione; la spedizione ha: 
#   - un identificativo (che deve essere univoco - non possono esistere due o più ordini con lo stesso identificativo); l'identificativo  deve essere nel formato LLCCC (L=lettera, C=Cifra)
#   - un elenco di oggetti da spedire (es: "maglietta", "scarpe", "Cintura") - sono gli oggetti che servono per far partire la spedizione e vengono tutti inseriti dall'utente, 
#       nel momento in cui viene creata la spedizione. La lista non potrà poi essere più modificata
#   - un elenco di oggetti caricati (es: "maglietta", "scarpe", "Cintura") - inizialmente la spedizione non ha oggetti caricati. Possono essere caricati tramite l'opzione 3)
# 2) eliminare una spedizione: tramite il codice identificativo, l'utente può indicare la spedizione da eliminare
# 3) carica oggetto alla spedizione: tramite il codice identificativo, l'utente può caricare un oggetto alla spedizione andando ad alimentare la lista degli oggetti caricati. 
#   E' possibile caricare solo uno degli oggetti della lista oggetti da spedire. Se ad esempio nella spedizione gli oggetti da spedire sono maglietta, scarpe e cintura 
#   e l'utente prova a caricare una felpa, dovrà ricevere un errore. Stessa cosa se cerca di caricare un oggetto già presente
# 4) partenza spedizione: inserendo il codice identificativo, l'utente può far partire la spedizione; la spedizione può partire solo se la lista di oggetti caricati
#   contiene tutti gli oggetti della lista da spedire. Se no, viene mostrato un messaggio di errore; se si, la spedizione parte e quindi viene eliminata dalla lista delle spedizioni

from os import system
system("cls")
from random import choice, randint

def menu():
    print("inserisci 1 per creare una spedizione")
    print("inserisci 2 per aggiungere un elemento alla lista")
    print("inserisci 3 per caricare un elemento alla spedizione")
    print("inserisci 4 per far partire la spedizione")
    print("inserisci 5 per eliminare la spedizione")
    print("inserisci 6 per visulizzare i dati")
    print("inserisci 0 per uscire\n")
    scelta = input().strip()
    while scelta not in ("0", "1", "2", "3", "4", "5", "6"):
        scelta = input("scelta non valida: riprova ").strip()
    
    print()    
    return int(scelta)
    

def chiedi_oggetto(ogg):
    nuovo = input("inserisci il nome dell'oggeto da aggiungere alla lista: ").strip().lower()
    while len(nuovo) < 3 or len(nuovo) > 30 or nuovo in ogg:
        if nuovo in ogg:
            print("errore: l'oggetto è già presente nella lista ")
        else:
            print("errore: nome oggetto non valido (min 3 caratteri, max 30)")

        nuovo = input("inserisci il nome dell'oggeto da aggiungere alla lista: ").strip().lower()
    
    ogg.append(nuovo)
    print()

def aggiungi_oggetto(ogg, sped):
    nuovo = input("inserisci il nome dell'oggeto della lista da aggiungere alla spedizione: ").strip().lower()
    while nuovo not in ogg or nuovo in sped:
        if nuovo not in ogg:
            print("errore: questo elemento non fa parte della lista")
        else:
            print("errore: l'elemento è già presente nella spedizione")
            
        nuovo = input("inserisci il nome dell'oggeto della lista da aggiungere alla spedizione: ").strip().lower()
    
    sped.append(nuovo)
    print()    
    
def crea_id():
    iden = ""
    for i in range(2):
        iden += choice("abcdefghijklmnopqrstuvwxyz")
        
    for i in range(4):
        iden += str(randint(0, 9))
        
    return iden
    
def chiedi_id(iden):
    verifica = input("inserisci l'id: ").strip().lower()
    if verifica != iden:
        print("errore: l'id non corrisponde\n")
        return False
    
    else:
        print()
        return True

def elimina(ogg, sped):
    ogg.clear()
    sped.clear()
    return ""

def manda_spedizione(ogg, sped):
    verifica = True
    for i in ogg:
        if i not in sped:
            verifica = False
            break
    
    if verifica:
        print("spedizione effettuata con successo")
        elimina(ogg, sped)
        print()
        return True
    else:
        print("errore: gli oggetti della lista non corrispondono a quelli della spedizione")
        print()
        return False
    
def visulizza(ogg, sped, iden):
    if len(ogg) == 0:
        print("non sono presenti oggetti nella lista")
    else:
        for i in range(len(ogg)):
            if i != len(ogg) - 1:
                print(f"{i + 1}: {ogg[i]}", end = ", ")
            else:
                print(f"{i + 1}: {ogg[i]}")
                
    print()
    
    if len(sped) == 0:
        print("non sono presenti oggetti nella spedizione")
    else:
        for i in range(len(sped)):
            if i != len(sped) - 1:
                print(f"{i + 1}: {sped[i]}", end = ", ")
            else:
                print(f"{i + 1}: {sped[i]}")
    
    print()
                
    print(f"id: {iden}\n")
                   
sclt = None
iden = ""
oggetti = []
spedizione = []

while sclt != 0:
    sclt = menu()
    
    if sclt == 1:
        if iden != "":
            print("effettua o elimina questa spedizione prima di iniziarne un'altra\n")
        else:
            iden = crea_id()
            print(f"spedizione creata - id: {iden}\n")
            
    elif iden == "" and sclt != 0:
        print("devi prima creare una spedizione\n")
        
    elif sclt == 2:
        chiedi_oggetto(oggetti)
        
    elif sclt == 3:
        aggiungi_oggetto(oggetti, spedizione)
        
    elif sclt == 4:
        avanti = chiedi_id(iden)
        if avanti: 
            esito = manda_spedizione(oggetti, spedizione)
            if esito:
                iden = ""
                
    elif sclt == 5:
        avanti = chiedi_id(iden)
        if avanti:
            iden = elimina(oggetti, spedizione)
            print("spedizione eliminata\n")
            
    elif sclt == 6:
        visulizza(oggetti, spedizione, iden)