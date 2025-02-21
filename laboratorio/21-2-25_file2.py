from os import system
system("cls")

f = open("testo.txt", "r", encoding="utf-8")

conta = 0
for riga in f:
    conta += 1
    print(f"{conta} - {riga}", end="")

f.close()