# Realizzare un programma nella quale l'utente può eseguire queste operazioni:
# 1) creare una nuova spedizione; la spedizione ha: 
#   - un identificativo (che deve essere univoco - non possono esistere due o più ordini con lo stesso identificativo); l'identificativo  deve essere nel formato LLCCC (L=lettera, C=Cifra)
#   - un elenco di oggetti da spedire (es: "maglietta", "scarpe", "Cintura") - sono gli oggetti che servono per far partire la spedizione e vengono tutti inseriti dall'utente, 
#       nel momento in cui viene creata la spedizione. La lista non potrà poi essere più modificata
#   - un elenco di oggetti caricati (es: "maglietta", "scarpe", "Cintura") - inizialmente la spedizione non ha oggetti caricati. Possono essere caricati tramite l'opzione 3)
# 2) eliminare una spedizione: tramite il codice identificativo, l'utente può indicare la spedizione da eliminare
# 3) carica oggetto alla spedizione: tramite il codice identificativo, l'utente può caricare un oggetto alla spedizione andando ad alimentare la lista degli oggetti caricati. 
#   E' possibile caricare solo uno degli oggetti della lista oggetti da spedire. Se ad esempio nella spedizione gli oggetti da spedire sono maglietta, scarpe e cintura 
#   e l'utente prova a caricare una felpa, dovrà ricevere un errore. Stessa cosa se cerca di caricare un oggetto già presente
# 4) partenza spedizione: inserendo il codice identificativo, l'utente può far partire la spedizione; la spedizione può partire solo se la lista di oggetti caricati
#   contiene tutti gli oggetti della lista da spedire. Se no, viene mostrato un messaggio di errore; se si, la spedizione parte e quindi viene eliminata dalla lista delle spedizioni

from os import system
system("cls")

