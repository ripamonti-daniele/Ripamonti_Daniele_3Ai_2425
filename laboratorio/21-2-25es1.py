from os import system
system("cls")

nome_file = input("inserisci il nome del file: ")
try:
    f = open(nome_file, "r", encoding="utf-8")
    righe = f.read()

except FileNotFoundError:
    print("file non trovato")

else:
    parola = input("inserisci una parola o una frase presente nel testo: ")

    if parola in righe:
        print(f"parola/frase trovata {righe.count(parola)} volte")
    else:
        print("parola/frase non trovata")
