from os import system
system("cls")

f = open("testo.txt")
righe = f.read()

caratteri = len(righe)

if righe[0] == " ":
    parole = 0
else:
    parole = 1

for i in range(len(righe)):
    if i < len(righe) and righe[i] == " " and righe[i + 1] != " ":
        parole += 1
    elif i < len(righe) and righe[i] == "\n" and righe[i + 1] != "\n":
        parole += 1

print(f"il testo contiene {caratteri} caratteri e {parole} parole")

f.close()

