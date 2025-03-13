f = open("laboratorio\\template.txt", "r", encoding="utf-8")

riscrivi = {"%titoloPagina%": "doc1", "%colore%": "FF0000", "%nome%": "Daniele", "%cognome%": "Ripamonti"}

nuovo = ""

for i in f:
    for key in riscrivi:
        if key in i:
            i = i.replace(key, riscrivi[key])
            
    nuovo += i

f.close()

f = open("laboratorio\\template.txt", "w", encoding="utf-8")

f.write(nuovo)

f.close()
