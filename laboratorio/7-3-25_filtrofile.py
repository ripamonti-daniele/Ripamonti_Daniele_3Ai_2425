from os import system, listdir, path
system("cls")

f = listdir("Ripamonti_Daniele_3Ai_2425\laboratorio")

for i in f:
    percorso = path.join("Ripamonti_Daniele_3Ai_2425\laboratorio", i)
    if path.isdir(percorso):
        print(i)   

print()

formato = input("scegli il formato dei file che vuoi vedere: ").strip()

print(f"\nfile {formato} presenti nella cartella:")
for i in f:
    if i.endswith(formato):
        print(i)
