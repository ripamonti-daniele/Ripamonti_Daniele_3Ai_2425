import os
os.system("cls")

file = os.listdir(".")

print("file presenti nella cartella")
for i in file:
    print(i)

print("\nfile .py presenti nella cartella")
for i in file:
    if i.endswith(".py"):
        print(i)
