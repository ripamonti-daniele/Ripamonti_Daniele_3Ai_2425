from os import system
system("cls")

f = open("testo.txt")
righe = f.read()
caratteri = len(righe.replace(" ", "").replace("\n", ""))
f.close()

if righe[0] == " ":
    parole = 0
else:
    parole = 1

for i in range(len(righe)):
    if i < len(righe) - 1 and righe[i] == " " and righe[i + 1] != " ":
        parole += 1
        continue
    elif i < len(righe) - 1 and righe[i] == "\n" and righe[i + 1] != "\n" and righe[i + 1] != " ":
        parole += 1

print(f"il testo contiene {caratteri} caratteri e {parole} parole")
