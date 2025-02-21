import os
os.system("cls")

nome_file = input("inserisci il nome del file: ")
if os.path.exists(nome_file):
    f = open(nome_file, "r", encoding="utf-8")
    righe = f.read()
    
    censura = {"scemo": "s***o", "cretino": "c*****o", "stupido": "s*****o"}

    for key, value in censura.items():
        righe.replace(key, value)

    #crea nuovo file e inserisce il contenuto di righe

else:
    print("file non trovato")