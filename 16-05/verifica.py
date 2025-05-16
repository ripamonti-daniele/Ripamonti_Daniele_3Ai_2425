import flet as ft

def main(page: ft.Page):
    page.title = "Sonaggio"
    page.window.width = 800
    page.window.height = 700
    
    def visualizza_seconda_parte(e):
        nome.value = nome.value.strip()
        nome.value = nome.value.capitalize()
        nome.disabled = True
        inizia.disabled = True
        seconda_parte.visible = True
        descrizione.visible = True
        testo_console.visible = True
        for i in console:
            i.visible=True
        testo_gioco.visible = True
        giochi.visible = True
        divisore1.visible = True
        divisore2.visible = True
        anno.visible = True
        switch.visible = True
        conferma.visible = True
        contenitore.visible = True
        page.update()

    def controlli_nome(e):
        if len(nome.value) == 0:
            nome.label = "Inserisci il tuo nome per procedere"
            inizia.disabled = True

        elif not(e.data.replace(" ", "").isalpha()):
            nome.label = "Puoi inserire solo lettere e spazi"
            inizia.disabled = True

        elif len(nome.value) < 3 and len(nome.value) > 0:
            nome.label = "Nome troppo corto"
            inizia.disabled = True

        else:
            nomi = carica_nomi("risultati.txt")
            if nome.value.strip().capitalize() in nomi:
                nome.label = "Nome già inserito"
                inizia.disabled = True

            else:
                nome.label = "Nome intervistato"
                inizia.disabled = False

        page.update()
        
    def invio(e):
        if anno.value == None:
            page.open(dialog)
            page.update()

        else:
            dialog.title=ft.Text("Sondaggio inviato")
            dialog.content=ft.Text("Puoi chiudere questa pagina")
            page.open(dialog)
            page.update()
            salva("risultati.txt")

            conferma.disabled = True
            seconda_parte.visible = False
            descrizione.visible = False
            testo_console.visible = False
            for i in console:
                i.visible=False
            testo_gioco.visible = False
            giochi.visible = False
            divisore2.visible = False
            anno.visible = False
            switch.visible = False
            conferma.visible = False
            page.update()

            dati = carica("risultati.txt")
            statistiche = []
            utenti = 0

            for i in dati.keys():
                utenti += 1
                gioco = False
                if i == "sport":
                    gioco = True

                if gioco:
                    statistiche.append(ft.Text(f"Utenti che hanno {i}: {dati[i]}", size=20))

                else:
                    statistiche.append(ft.Text(f"Utenti che preferiscono i giochi {i}: {dati[i]}", size=20))

            statistiche.append(ft.Text(f"Utenti totali: {utenti}", size=20))

            contenitore.content=ft.Column(
                statistiche
            )

            page.update()

    def salva(path):
        continua = True
        try:
            f = open(path, "a", encoding="utf-8")
        except:
            continua = False
            print("file non trovato")

        if continua:
            f.write(f"{nome.value}|{anno.value}|{console[0].value}|{console[1].value}|{console[2].value}|{console[3].value}|{console[4].value}|{giochi.value}|{switch.value}\n")

    def carica(path):
        continua = True
        try:
            f = open(path, "r", encoding="utf-8")
        except:
            continua = False
            print("file non trovato")

        if continua:
            dati = {"xbox": 0, "psx": 0, "switch": 0, "pc": 0, "android/ios": 0, "sport": 0, "platform": 0, "rpg": 0, "fps": 0}
            for r in f:
                r = r.replace("\n", "")
                elementi = r.split("|")

                for i in range(2, len(elementi) - 1):
                    if elementi[i] == "True":
                        if i == 2:
                            dati["xbox"] += 1
                        elif i == 3:
                            dati["switch"] += 1
                        elif i == 4:
                            dati["pc"] += 1
                        elif i == 5:
                            dati["android/ios"] += 1
                    
                    elif elementi[i] == 1:
                        dati["sport"] += 1
                    elif elementi[i] == 2:
                        dati["platfrom"] += 1
                    elif elementi[i] == 3:
                        dati["rpg"] += 1
                    elif elementi[i] == 4:
                        dati["fps"] += 1

            return dati

    def carica_nomi(path):
        continua = True
        try:
            f = open(path, "r", encoding="utf-8")
        except:
            continua = False
            print("file non trovato")

        if continua:
            nomi = []
            for r in f:
                r = r.replace("\n", "")
                elementi = r.split("|")
                nomi.append(elementi[0])

            return nomi


    nome = ft.TextField(label="Inserisci il tuo nome per procedere", icon=ft.Icons.SUPERVISED_USER_CIRCLE, width=500, on_change=controlli_nome)
    inizia = ft.ElevatedButton(text="Inizia", icon=ft.Icons.SEARCH, width=150, color="white", bgcolor="#1345A7", icon_color="white", on_click=visualizza_seconda_parte, disabled=True)
    seconda_parte = ft.Text("Seconda parte", size=25, weight=ft.FontWeight.BOLD, visible=False)
    descrizione = ft.Text("Accoda le preferenze nel file sondaggio.txt.", size=15, italic=True, visible=False)

    testo_console = ft.Text("Sistemi di gioco a disposizione:", size=18, visible=False)
    console = [
        ft.Checkbox(label="Xbox", value="xbox", visible=False),
        ft.Checkbox(label="Psx", value="psx", visible=False),
        ft.Checkbox(label="Switch", value="switch", visible=False),
        ft.Checkbox(label="Pc", value="pc", visible=False),
        ft.Checkbox(label="Android/Ios", value="android/ios", visible=False),
    ]

    testo_gioco = ft.Text("Tipologia di gioco preferita:", size=18, visible=False)
    giochi = ft.RadioGroup(visible=False, content=ft.Row(
        [
            ft.Radio(label="Nessuna", value=None),
            ft.Radio(label="Sport", value=1),
            ft.Radio(label="Platform", value=2),
            ft.Radio(label="Rpg", value=3),
            ft.Radio(label="Fps", value=4)
        ]
    ))

    divisore1 = ft.Divider(visible=False)
    divisore2 = ft.Divider(visible=False)

    anno = ft.Dropdown(
        label="Quale anno frequenti?",
        width=400,
        options=[ft.DropdownOption(i) for i in ("1°", "2°", "3°", "4°", "5°")],
        visible=False
    )

    switch = ft.Switch(
        label="Acconsento all'invio delle promozioni pubblicitarie",
        value=False,
        visible=False,
        label_style=ft.TextStyle(size=18)
    )

    conferma = ft.ElevatedButton(text="Conferma", icon=ft.Icons.BOOKMARK_ADDED, visible=False, width=600, color="white", bgcolor="#1345A7", icon_color="white", on_click=invio)

    contenitore = ft.Container(visible=False, width=600, height="auto", padding=20, margin=10, border=ft.border.all(1, ""), border_radius=5, content=ft.Column(
            [
                testo_console,
                ft.Row(console),
                testo_gioco,
                giochi,
                divisore2,
                anno,
                switch,
                conferma

            ]
        )
    )

    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Attenzione"),
        content=ft.Text("Devi inserire il tuo anno per procedere"),
        actions=[ft.TextButton("Ok", on_click=lambda e: page.close(dialog)),],
        )

    page.add(
        ft.Column(
            [
                ft.Text("Prima parte", size=25, weight=ft.FontWeight.BOLD),
                ft.Text("Verifica che il nome dell'intervistato non sia già stato utlizzato.", size=15, italic=True),
                ft.Row(
                    [
                        nome, inizia   
                    ],
                ),
                divisore1,
                seconda_parte,
                descrizione,
                contenitore
            ]
        )
    )

ft.app(main)