# visualizza i pacchtti numerando i pacchetti
# aggiungi nuova offerta di viaggio (con controlli)
# modifica il prezzo di un pacchetto specifico
# visualizza i pacchetti relativi a una specifica destinazione (prezzo crescente)

from os import system
system("cls")

import datetime

pacchetti = [
    {'nome':'Parigi', 'prezzo':500, 'inizio':'3/05/2025', 'fine':'10/05/2025', 'posti':10},
    {'nome':'Londra', 'prezzo':520, 'inizio':'11/05/2025', 'fine':'16/05/2025', 'posti':2},
    {'nome':'Barcellona', 'prezzo':380, 'inizio':'13/06/2025', 'fine':'15/06/2025', 'posti':12},
    {'nome':'Amsterdam', 'prezzo':650, 'inizio':'14/04/2025', 'fine':'19/04/2025', 'posti':5},
    {'nome':'Amsterdam', 'prezzo':600, 'inizio':'25/05/2025', 'fine':'1/06/2025', 'posti':8}]

def visualizza(lista):
    ind = 0
    for i in lista:
        ind += 1
        print(f"{ind}) destinazione:", i["nome"])
        print("   prezzo:", i["prezzo"], "euro")
        print("   data inizio:", i["inizio"])
        print("   data fine:", i["fine"])
        print("   posti:", i["posti"], "\n")

def chiedi_luogo():
    while True:
        luogo = input("inserisci la destinazione: ").strip().capitalize()
        if len(luogo) == 0:
            print("errore: devi scrivere almeno un carattere")
        else:
            return luogo

def chiedi_prezzo(msg = "il prezzo", tipo = float):
    while True:
        try:
            p = tipo(input(f"inserisci {msg}: ").strip())
        except ValueError:
            print("errore: devi inserire un numero con formato valido")
            continue
        except:
            print("errore")
            continue
        
        if p < 0:
            print("errore: non puoi inserire un numero negativo")
        else:
            return p

def chiedi_data(futura, msg = ""):
    while True:
        d = input("inserisci la data " + msg + " nel formato gg-mm-aaaa: ").strip()
        try:
            d = datetime.datetime(int(d[6:]), int(d[3:5]), int(d[:2]))
        except:
            print("formato data non valido")
            continue

        if futura:
            oggi = datetime.datetime.now()

            if (d - oggi).days >= -1:
                d = str(d.date())
                return d[8:] + "/" + d[5:7] + "/" + d[:4]
            else:
                print("errore: questa data è già passata")

        else:
            d = str(d.date())
            return d[8:] + "/" + d[5:7] + "/" + d[:4]

def nuova(lista):
    nome = chiedi_luogo()
    p = chiedi_prezzo()

    errore = True
    while errore:
        data_iniziale = chiedi_data(True, "iniziale")
        data_finale = chiedi_data(True, "finale")

        if int(data_iniziale[6:]) > int(data_finale[6:]):
            print("errore: la data finale deve essere futura a quella iniziale")
            continue
        elif int(data_iniziale[6:]) < int(data_finale[6:]):
            errore = False
            continue
        else:
            if int(data_iniziale[3:5]) > int(data_finale[3:5]):
                print("errore: la data finale deve essere futura a quella iniziale")
                continue
            elif int(data_iniziale[3:5]) < int(data_finale[3:5]):
                errore = False
                continue
            else:
                if int(data_iniziale[:2]) >= int(data_finale[:2]):
                    print("errore: la data finale deve essere futura a quella iniziale")
                    continue
                else:
                    errore = False

    posti = chiedi_prezzo(msg = "i posti disponibili", tipo = int)
    while posti > 100:
        print("numero posti non valido")
        posti = chiedi_prezzo(msg = "i posti disponibili", tipo = int)

    lista.append({'nome': nome, 'prezzo':p, 'inizio':data_iniziale, 'fine':data_finale, 'posti':posti})

def modifica_prezzo(lista):
    l = []
    for i in lista:
        l.append(i["nome"])

    luogo = chiedi_luogo()
    while luogo not in l:
        print("errore: destinazione non trovata")
        luogo = chiedi_luogo()
    
    esito = False
    ind = -1
    data = chiedi_data(False, "iniziale")
    for i in lista:
        ind += 1
        if i["nome"] == luogo:
            if i["inizio"] == data:
                esito = True
                break

    if esito:
        p = chiedi_prezzo()
        lista[ind]["prezzo"] = p

    else:
        print("errore: la data non corrisponde")

def bubble_sort(lista):
    for j in range(len(lista) - 1):
        for i in range(len(lista) - 1 - j):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]

def visualizza_per_luogo(lista):
    luogo = chiedi_luogo()
    l = []
    for i in lista:
        if i["nome"] == luogo:
            l.append((i["prezzo"], i["nome"], i["inizio"], i["fine"], i["posti"]))

    bubble_sort(l)
    ind = 0
    for i in l:
        ind += 1
        print(f"{ind}) destinazione:", i[1])
        print("   prezzo:", i[0], "euro")
        print("   data inizio:", i[2])
        print("   data fine:", i[3])
        print("   posti:", i[4], "\n")

def menu():
    print("inserisci 1 per visualizzare i pacchetti")
    print("inserisci 2 per aggiungere un pacchetto")
    print("inserisci 3 per modificare il prezzo di un pacchetto")
    print("inserisci 4 per visualizzare i pacchetti con una stessa destinazione")
    print("inserisci 0 per uscire")

    opzioni = ("0", "1", "2", "3", "4")
    sclt = input().strip()
    while sclt not in opzioni:
        print("scelta non valida")
        sclt = input().strip()

    return int(sclt)

sclt = -1
while sclt != 0:
    sclt = menu()
    match sclt:
        case 1:
            visualizza(pacchetti)
        case 2:
            nuova(pacchetti)
        case 3:
            modifica_prezzo(pacchetti)
        case 4:
            visualizza_per_luogo(pacchetti)

    print()
