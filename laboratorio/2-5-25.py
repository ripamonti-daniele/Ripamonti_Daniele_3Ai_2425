# programma che ci fa prenotare i posti al cinema 
# scegli il film, il posto, sala 2d o 3d, data e ora

import flet as ft
import datetime

def main(page: ft.Page):
    page.title = "Prenotazione Cinema"

    def controlli_nome(e):
        global controlli
        if e.data.isalpha() and len(e.data) >= 3 and len(e.data) <= 15:
            controlli["nome"] = True
        else:
            controlli["nome"] = False

    def controlli_cognome(e):
        global controlli
        if e.data.isalpha() and len(e.data) >= 3 and len(e.data) <= 20:
            controlli["cognome"] = True
        else:
            controlli["cognome"] = False

    def attiva_data(e):
        global controlli
        opzioni = []
        for i in film[e.data]: 
            opzioni.append("Data " + str(i["data"].strftime("%d-%m-%Y\nOra %H:%M")) + "\nDurata " + i["durata"] + "h\nSala " + str(i["sala"]) + "\nVisione " + i["visione"] + "\n")

        scegli_data.options = [ft.dropdown.Option(i) for i in opzioni]

        scegli_data.disabled = False
        scegli_data.value = None
        scegli_colonna.disabled = True
        scegli_riga.disabled = True
        controlli["film"] = True
        controlli["data"] = False
        controlli["riga"] = False
        controlli["colonna"] = False
        page.update()

    def attiva_posto(e):
        global controlli
        for i, opzione in enumerate(scegli_data.options):
            if opzione.key == scegli_data.value:
                indice = i
                break

        colonne = []
        for i in range(film[scegli_film.value][indice]["colonne"]):
            colonne.append(i + 1)

        righe = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]
        righe = righe[:film[scegli_film.value][indice]["righe"]]

        scegli_colonna.options = [ft.dropdown.Option(i) for i in colonne]
        scegli_riga.options = [ft.dropdown.Option(i) for i in righe]

        scegli_colonna.disabled = False
        scegli_colonna.value = None
        scegli_riga.disabled = False
        scegli_riga.value = None
        controlli["data"] = True
        controlli["riga"] = False
        controlli["colonna"] = False
        page.update()

    def colonna_scelta(e):
        global controlli
        controlli["colonna"] = True

    def riga_scelta(e):
        global controlli
        controlli["riga"] = True

    def verifica(e):
        global controlli
        errori = False
        titolo = "Attenzione"
        testo = "Errori nella compilazione di "
        for i in controlli.keys():
            if controlli[i] == False:
                errori = True
                testo += i + ", "
        
        testo = testo[:-2]

        if not errori:
            titolo = "Prentotazione eseguita"
            testo = "Prenotazione eseguita con successo"

        info = ft.AlertDialog(
            modal=True,
            title=ft.Text(titolo),
            content=ft.Text(testo, size = 18),
            actions=[ft.TextButton("Ok", on_click=lambda e: page.close(info), scale=1.3)]
        )

        page.open(info)
        page.update()

    film = {
        "Avengers": [{"data" :datetime.datetime(2025, 2, 10, 20, 0), "durata": "2:30", "sala": 1, "visione": "2d", "colonne": 10, "righe": 10}, {"data" :datetime.datetime(2025, 2, 15, 15, 30), "durata": "2:30", "sala": 7, "visione": "3d", "colonne": 15, "righe": 15}],
        "Spiderman": [{"data" :datetime.datetime(2025, 2, 8, 18, 30), "durata": "2:00", "sala": 4, "visione": "3d", "colonne": 15, "righe": 15}, {"data" :datetime.datetime(2025, 2, 12, 20, 0), "durata": "2:00", "sala": 1, "visione": "2d", "colonne": 10, "righe": 10}],
        "Barbie": [{"data" :datetime.datetime(2025, 2, 20, 16, 30), "durata": "2:00", "sala": 5, "visione": "2d", "colonne": 10, "righe": 10}],
        "Batman": [{"data" :datetime.datetime(2025, 2, 17, 21, 0), "durata": "3:00", "sala": 2, "visione": "2d", "colonne": 10, "righe": 10}]
    }

    global controlli
    controlli = {"nome": False, "cognome": False, "film": False, "data": False, "riga": False, "colonna": False}

    nome = ft.TextField(label="Nome", width=400, on_change=controlli_nome)
    cognome = ft.TextField(label="Cognome", width=400, on_change=controlli_cognome)

    scegli_film = ft.Dropdown(
        width=400,
        label="Scegli un film",
        options=[
            ft.dropdown.Option(i)
            for i in film.keys()
        ],
        on_change=attiva_data
    )

    scegli_data = ft.Dropdown(
        disabled=True,
        width=400,
        label="Scegli una data",
        on_change=attiva_posto,
    )

    scegli_colonna = ft.Dropdown(
        disabled=True,
        width=400,
        label="Scegli una colonna",
        on_change=colonna_scelta
    )

    scegli_riga = ft.Dropdown(
        disabled=True,
        width=400,
        label="Scegli una riga",
        on_change=riga_scelta
    )

    page.add(
        ft.Row(
            [
                ft.Text("Prenotazione Cinema", size=50, weight=ft.FontWeight.BOLD, color="red")
            ], alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                nome, cognome
            ], alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                scegli_film, scegli_data
            ], alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                scegli_colonna, scegli_riga
            ], alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.Button(text="Invio", on_click=verifica, width=150, height=50, style=ft.ButtonStyle(text_style=ft.TextStyle(size=20)), bgcolor="#ffff66")
            ], alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(main)