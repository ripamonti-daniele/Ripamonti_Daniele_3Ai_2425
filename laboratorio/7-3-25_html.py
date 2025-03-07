f = open("Ripamonti_Daniele_3Ai_2425\\laboratorio\\template.txt", "r", encoding="utf-8")
testo = f.read()

# parole = testo.split()

riscrivi = {"%titoloPagina%": "doc1", "%colore%": "FF0000", "%nome%": "Daniele", "%cognome%": "Ripamonti"}
conto_perc = 0
for j, i in enumerate(testo):
    t = ""
    pos = 0
    if i == "%" and (conto_perc % 2 == 0 or conto_perc == 0):
        t += testo[pos:j]
        pos = j
        conto_perc += 1
        # print("a", conto_perc, pos)
           
    if i == "%" and conto_perc != 0 and conto_perc % 2 != 0:
        print(testo[pos:j + 1], j + 1, pos)
        conto_perc += 1
        # print("ok", conto_perc)
        if testo[pos:j + 1] in riscrivi:
            t += riscrivi[testo[pos:j + 1]]
            print("ok")  
        pos = j + 1

# print(t)