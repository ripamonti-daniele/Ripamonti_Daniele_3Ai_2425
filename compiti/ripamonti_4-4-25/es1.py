from os import system
system("cls")

schede_video = {}

def chiedi_scheda(d, nuova=False):
    while True:
        scheda = input("inserisci il nome della marca della scheda video: ").strip().capitalize()
        if len(scheda) < 2 or len(scheda) > 15:
            print("lunghezzza non valida")
            continue
        
        if not(nuova) and scheda not in d:
            print("scheda non trovata")
            
        else:
            return scheda
        
def chiedi_modello(d, scheda, nuova=False, msg = ""):
    while True:
        modello = input(f"inserisci il nome del modello della {msg} scheda video: ").strip().capitalize()
        if len(modello) < 2 or len(modello) > 15:
            print("lunghezzza non valida")
            continue
        
        if not(nuova) and modello not in d[scheda]:
            print("modello non trovato")
            
        elif nuova and modello in d[scheda]:
            print("modello già inserito")
            
        else:
            return modello
      
def nuova(d):
    scheda = chiedi_scheda(d, True)
    if scheda not in d:
        d[scheda] = []
    modello = chiedi_modello(d, scheda, True)
    d[scheda].append(modello)

def elimina(d):
    scheda = chiedi_scheda(d)
    modello = chiedi_modello(d, scheda)
    d[scheda].remove(modello)

def modifica(d):
    scheda = chiedi_scheda(d)
    modello_vecchio = chiedi_modello(d, scheda, msg="vecchia")
    modello_nuovo = chiedi_modello(d, scheda, True, msg="nuova")
    d[scheda][d[scheda].index(modello_vecchio)] = modello_nuovo

def visualizza(d):
    if len(d) == 0:
        print("nessuna scheda video trovata\n")
    else:
        ind = 0
        for i in d.keys():
            ind += 1
            print(ind, i + ":")
            for j in d[i]:
                print("-", j)
            print()

def carica(path, d):
    f = open(path, "r", encoding="utf-8")
    pos = 0
    for r in f:
        key = ""
        for i in range(15, len(r), 15):
            f.readline()
            f.seek(i + pos - 15)
            if i == 15: 
                key = f.read(15).strip()
                d[key] = []
            else:
                d[key].append(f.read(15).strip())
                
        pos += len(r)
    
    print("dati caricati")
    f.close()

def salva(path, d):
    f = open(path, "w", encoding="utf-8")
    for i in d.keys():
        r = i
        r += " " * (15 - len(r))
        
        for j in d[i]:
            s = j
            s += " " * (15 - len(s))
            r += s
            
        f.write(r + "\n")
        
    print("dati salvati")
    f.close()
    
def menu():
    print("inserisci 1 per aggiungere una scheda video")
    print("inserisci 2 per eliminare una scheda video")
    print("inserisci 3 per modificare una scheda video")
    print("inserisci 4 per visualizzare le schede video")
    print("inserisci 5 per caricare i dati")
    print("inserisci 6 per slavare i dati")
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
            nuova(schede_video)
            print()
        case 2:
            elimina(schede_video)
            print()
        case 3:
            modifica(schede_video)
            print()
        case 4:
            visualizza(schede_video)
        case 5:
            carica("compiti\\ripamonti_4-4-25\\archivio_schede_video.txt", schede_video)
            print()
        case 6:
            salva("compiti\\ripamonti_4-4-25\\archivio_schede_video.txt", schede_video)
            print()
