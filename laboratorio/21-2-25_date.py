from os import system
system("cls")

import datetime

oggi = datetime.datetime.now()
d = datetime.datetime(2008, 2, 12)

print(d.strftime("%d-%m-%Y"))
print(oggi.strftime("%d-%m-%Y"))

diff = oggi - d

print(diff)

if diff.days >= 6200:
    print("puoi partecipare")

else:
    print("sei troppo piccolo/a")

errore = True
while errore:
    s = input("inserisci la data di acquisto della tua psx nel formato gg-mm-aaaa: ")
    try:
        sc = datetime.datetime.strptime(s, "%d-%m-%Y")
        errore = False
    except ValueError:
        print("formato data non valido")
    except:
        print("errore")

diff = oggi - sc

print(f"la tua play ha {diff.days} giorni")
