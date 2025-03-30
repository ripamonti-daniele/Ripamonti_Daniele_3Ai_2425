# app che chiede nome e cognome, la classe, gli sport, il sesso, anno di nascita
# per l'iscrizione al campionato di fine anno

# ci si può iscrivere a un solo sprt tra calcio, basket, ping pong (anche misti) e atletica
# console preferita tra psx, xbox, switch

# effettua gli eventuali controlli sui dati inseriti e visualizza un riepilogo delle informazioni collezionate

import flet as ft

def main(page: ft.Page):
    page.title = "Inscrizione Tornei Fine Anno"
    ft.VerticalAlignment = ft.MainAxisAlignment.START

    # funzioni
    
    def controllo_nome(e):
        if len(e.data) > 0 and not(e.data.isalpha()):
            msg_nome.value = "Errore: caratteri non validi"
            
        elif len(e.data) < 2 and len(e.data) > 0:
            msg_nome.value = "Errore: nome troppo corto"
        
        elif len(e.data) > 20:
            msg_nome.value = "Errore: nome troppo lungo"
            
        else:
            msg_nome.value = ""
            
        msg_nome.update()
        
    def controllo_cognome(e):
        if len(e.data) > 0 and not(e.data.isalpha()):
            msg_cognome.value = "Errore: caratteri non validi"
            
        elif len(e.data) < 2 and len(e.data) > 0:
            msg_cognome.value = "Errore: cognome troppo corto"
        
        elif len(e.data) > 20:
            msg_cognome.value = "Errore: cognome troppo lungo"
            
        else:
            msg_cognome.value = ""
            
        msg_cognome.update()
        
    def controllo_anno(e):
        if len(e.data) == 0:
            msg_anno.value = ""
        else:
            try:
                anno = int(e.data)
            except ValueError:
                msg_anno.value = "Errore: inserisci un numero intero"
            else:
                if anno < 2003 or anno > 2011:
                    msg_anno.value = "Errore: anno non accettabile"
                else:
                    msg_anno.value = ""
            
        msg_anno.update()
            
    def modifica(e):
        opzioni.disabled = False
        opzioni.options = [
            ft.dropdown.Option(i)
            for i in sezioni[int(classe.value) - 1]
        ]
        opzioni.update()
        
    def invia(e):
        msg = ""
        colore = "#ff0000"
        if len(txt_nome.value) == 0 or msg_nome.value != "":
            msg = "Errore: nome non valido"
        elif len(txt_cognome.value) == 0 or msg_cognome.value != "":
            msg = "Errore: cognome non valido"
        elif len(txt_anno.value) == 0 or msg_anno.value != "":
            msg = "Errore: anno di nascita non valido"
        elif scelta_sesso.value == None:
            msg = "Errore: indica il tuo sesso"  
        elif scelta_sport.value == None:
            msg = "Errore: scegli un torneo"  
        elif scelta_console.value == None:
            msg = "Errore: indica la tua console preferita"  
        elif classe.value == None:
            msg = "Errore: scegli la tua classe"  
        elif opzioni.value == None:
            msg = "Errore: scegli la tua sezione"
        elif opzioni.value not in sezioni[int(classe.value) - 1]:
            msg = "Errore: sezione non valida"
        else:
            msg = "Iscrizione inviata"
            colore = "#00ff00"
            
        msg_invio.value = msg
        msg_invio.color = colore
        msg_invio.update()
    
    # variabili
        
    txt_nome = ft.TextField(label="Nome", on_change=controllo_nome)
    msg_nome = ft.Text("", color="#ff0000", size=18, weight=ft.FontWeight.BOLD)
    
    txt_cognome = ft.TextField(label="Cognome", on_change=controllo_cognome)
    msg_cognome = ft.Text("", color="#ff0000", size=18, weight=ft.FontWeight.BOLD)
    
    txt_anno = ft.TextField(label="Anno di nascita", on_change=controllo_anno)
    msg_anno = ft.Text("", color="#ff0000", size=18, weight=ft.FontWeight.BOLD)
    
    scelta_sesso = ft.RadioGroup(content=ft.Row(
        [
        ft.Radio(value="Uomo", label="Uomo", scale=1.1),
        ft.Radio(value="Donna", label="Donna", scale=1.1),
        ]))

    sezioni = [["A", "B", "C", "D", "E", "F", "G", "H", "Z"], 
              ["A", "B", "C", "D", "E", "F", "G", "H", "I", "L"],
              ["Al", "Aa", "Ac", "Ae", "Ai", "At", "Ba", "Bi"],
              ["Aa", "Ac", "Ae", "Ai", "An", "At", "Ba", "Bi", "Ci"],
              ["Al", "Aa", "Ac", "Ae", "Ai", "An", "At", "Ba", "Bi", "Ci"]]
    
    classe = ft.RadioGroup(content=ft.Row(
        [
        ft.Radio(value=1, label="1", scale=1.1),
        ft.Radio(value=2, label="2", scale=1.1),
        ft.Radio(value=3, label="3", scale=1.1),
        ft.Radio(value=4, label="4", scale=1.1),
        ft.Radio(value=5, label="5", scale=1.1)
        ]), on_change=modifica)
    
    opzioni = ft.Dropdown(
        disabled=True,
        width=300,
        label="Scegli la tua sezione"
    )

    scelta_sport = ft.RadioGroup(content=ft.Column(
        [
        ft.Radio(value="Calcio", label="Calcio", scale=1.1),
        ft.Radio(value="Basket", label="Basket", scale=1.1),
        ft.Radio(value="Ping Pong", label="Ping Pong", scale=1.1),
        ft.Radio(value="Atletica", label="Atletica", scale=1.1)
        ]))

    scelta_console = ft.RadioGroup(content=ft.Column(
        [
        ft.Radio(value="PlayStation", label="PlayStation", scale=1.1),
        ft.Radio(value="Xbox", label="Xbox", scale=1.1),
        ft.Radio(value="Switch", label="Switch", scale=1.1),
        ])) 
    
    invio = ft.Button(text="Invio", on_click=invia, width=150, height=50, style=ft.ButtonStyle(text_style=ft.TextStyle(size=20)), bgcolor="#ffff66")
    msg_invio = ft.Text("", size=25, color="#ff0000", weight=ft.FontWeight.BOLD)

    # messa a schermo
 
    page.add(
        ft.Row(
            [
                ft.Text(
                    "Iscrizione Tornei Fine Anno",
                    size=40,
                    weight=ft.FontWeight.BOLD,
                    color="#0000FF",
                    italic=True
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        
        ft.Container(padding=ft.padding.only(top=20)),

        ft.Row(
            [
                ft.Column(
                    [
                        txt_nome,
                        msg_nome,
                    ], 
                    alignment=ft.MainAxisAlignment.START
                ),

                ft.Column(
                    [
                        txt_cognome,
                        msg_cognome,
                    ], 
                    alignment=ft.MainAxisAlignment.START
                ),

                ft.Column(
                    [
                        txt_anno,
                        msg_anno,
                    ], 
                    alignment=ft.MainAxisAlignment.START
                ),
                
                ft.Container(padding=ft.padding.only(right=10)),

                ft.Column(
                    [
                        ft.Text("Sesso", size=20, weight=ft.FontWeight.BOLD),
                        scelta_sesso
                    ], 
                    alignment=ft.MainAxisAlignment.START
                ),
            ], 
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.START
        ),
        
        ft.Container(padding=ft.padding.only(top=10)),
        
        ft.Row(
            [
                ft.Column(
                    [
                        ft.Text("Classe", size=18, weight=ft.FontWeight.BOLD),
                        classe,
                        ft.Text("Sezione", size=18, weight=ft.FontWeight.BOLD),
                        opzioni
                    ], 
                    alignment=ft.MainAxisAlignment.START
                ),
                
                ft.Container(padding=ft.padding.only(right=10)),

                ft.Column(
                    [
                        ft.Text("Torneo al quale vuoi partecipare", size=20, weight=ft.FontWeight.BOLD),
                        scelta_sport
                    ], 
                    alignment=ft.MainAxisAlignment.START
                ),
                
                ft.Container(padding=ft.padding.only(right=10)),

                ft.Column(
                    [
                        ft.Text("Scegli la tua console preferita", size=20, weight=ft.FontWeight.BOLD),
                        scelta_console
                    ], 
                    alignment=ft.MainAxisAlignment.START
                ),
            ], 
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.START
        ),
        
        ft.Container(padding=ft.padding.only(top=40)),
        
        ft.Row(
            [
                ft.Column(
                    [
                        msg_invio,
                        invio,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ], 
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(main)