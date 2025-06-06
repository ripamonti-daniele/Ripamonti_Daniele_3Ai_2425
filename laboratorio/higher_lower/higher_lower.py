import flet as ft
from random import shuffle

def main(page: ft.Page):
    page.title = "Higer or lower"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.width = 1400
    page.window.height = 1000

    artisti = {}
    ordine_artisti = []
    global indice
    indice = 0

    def carica(path, d):
        avanti = False
        try:
            f = open(path, "r", encoding="utf-8")
            avanti = True
        except:
            print("file non trovato")

        if avanti:
            for r in f:
                r = r.replace("\n", "")
                elementi = r.split("|")
                d[elementi[0]] = (int(elementi[1]), elementi[2])

    def higher(e):
        prossimo_btn.disabled = False
        ascoltatori2.visible = True
        asc2.visible = True
        higher_btn.disabled = True
        lower_btn.disabled = True
        if int(ascoltatori1.value) < int(ascoltatori2.value):
            testo.value = "CORRETTO"
            testo.color = "#2dc22b"

        else:
            testo.value = "SBAGLIATO"
            testo.color = "#e91b21"
            prossimo_btn.text = "Fine"
            prossimo_btn.on_click = reset

        page.update()

    def lower(e):
        higher_btn.disabled = True
        lower_btn.disabled = True
        prossimo_btn.disabled = False
        ascoltatori2.visible = True
        asc2.visible = True
        if int(ascoltatori1.value) > int(ascoltatori2.value):
            testo.value = "CORRETTO"
            testo.color = "#2dc22b"

        else:
            testo.value = "SBAGLIATO"
            testo.color = "#e91b21"
            prossimo_btn.text = "Fine"
            prossimo_btn.on_click = reset

        page.update()

    def Inizia(e):
        global indice
        prossimo_btn.disabled = True
        img1.visible = True
        img2.visible = True
        ascoltatori1.visible = True
        asc1.visible = True
        higher_btn.visible = True
        lower_btn.visible = True
        nome1.visible = True
        nome2.visible = True
        prossimo_btn.text="Successivo"
        prossimo_btn.on_click=successivo

        carica("dati.txt", artisti)
        for i in artisti.keys():
            ordine_artisti.append(i)
        shuffle(ordine_artisti)

        img1.src = artisti[ordine_artisti[indice]][1]
        ascoltatori1.value = str(artisti[ordine_artisti[indice]][0])
        nome1.value = ordine_artisti[indice]

        indice += 1

        img2.src = artisti[ordine_artisti[indice]][1]
        ascoltatori2.value = str(artisti[ordine_artisti[indice]][0])
        nome2.value = ordine_artisti[indice]

        page.update()


    def successivo(e):
        global indice

        if indice < len(ordine_artisti) - 1:
            prossimo_btn.disabled = True
            ascoltatori2.visible = False
            asc2.visible = False
            higher_btn.disabled = False
            lower_btn.disabled = False
            testo.value = "HIGHER OR LOWER"
            testo.color = "#0000FF"
            img1.src = artisti[ordine_artisti[indice]][1]
            ascoltatori1.value = str(artisti[ordine_artisti[indice]][0])
            nome1.value = ordine_artisti[indice]

            indice += 1

            img2.src = artisti[ordine_artisti[indice]][1]
            ascoltatori2.value = str(artisti[ordine_artisti[indice]][0])
            nome2.value = ordine_artisti[indice]

        else:
            testo.value = "HAI VINTO"
            testo.color = "#2dc22b"
            prossimo_btn.text = "Fine"
            prossimo_btn.on_click = reset

        page.update()

    def reset(e):
        global indice
        indice = 0
        img1.visible = False
        img2.visible = False
        ascoltatori1.visible = False
        asc1.visible = False
        ascoltatori2.visible = False
        asc2.visible = False
        higher_btn.visible = False
        lower_btn.visible = False
        nome1.visible = False
        nome2.visible = False
        higher_btn.disabled = False
        lower_btn.disabled = False
        prossimo_btn.text = "Inizia"
        prossimo_btn.on_click=Inizia
        testo.value = "HIGHER OR LOWER"
        testo.color = "#0000FF"
        dati = {}
        ordine_artisti.clear()

        page.update()


    testo = ft.Text("HIGHER OR LOWER", size=80, weight=ft.FontWeight.BOLD, color="#0000FF",)

    img1 = ft.Image(src="", width=500, height=500, fit=ft.ImageFit.CONTAIN, visible=False)
    img2 = ft.Image(src="", width=500, height=500, fit=ft.ImageFit.CONTAIN, visible=False)

    ascoltatori1 = ft.Text("", size=40, weight=ft.FontWeight.BOLD, color="#e1a42b", visible=False)
    ascoltatori2 = ft.Text("", size=40, weight=ft.FontWeight.BOLD, color="#e1a42b", visible=False)
    asc1 = ft.Text("ascoltatori", size=40, weight=ft.FontWeight.BOLD, color="#e1a42b", visible=False)
    asc2 = ft.Text("ascoltatori", size=40, weight=ft.FontWeight.BOLD, color="#e1a42b", visible=False)

    nome1 = ft.Text("", size=40, weight=ft.FontWeight.BOLD, color="#8b0000", visible=False)
    nome2 = ft.Text("", size=40, weight=ft.FontWeight.BOLD, color="#8b0000", visible=False)

    higher_btn = ft.ElevatedButton(text="Higher", on_click=higher, width=150, height=50, style=ft.ButtonStyle(text_style=ft.TextStyle(size=20)), bgcolor="#ffff66", visible=False)
    lower_btn = ft.ElevatedButton(text="Lower", on_click=lower, width=150, height=50, style=ft.ButtonStyle(text_style=ft.TextStyle(size=20)), bgcolor="#ffff66", visible=False)

    prossimo_btn = ft.ElevatedButton(text="Inizia", on_click=Inizia, width=150, height=50, style=ft.ButtonStyle(text_style=ft.TextStyle(size=20)), bgcolor="#ffff66")



    page.add(
        ft.Row([testo], alignment=ft.MainAxisAlignment.CENTER),

        ft.Row([
            ft.Column([nome1, img1, ft.Row([ascoltatori1, asc1])], horizontal_alignment=ft.MainAxisAlignment.END),
            ft.Column([higher_btn, lower_btn], horizontal_alignment=ft.MainAxisAlignment.CENTER),
            ft.Column([nome2, img2, ft.Row([ascoltatori2, asc2])], horizontal_alignment=ft.MainAxisAlignment.CENTER)
        ], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.MainAxisAlignment.CENTER),

        ft.Row([
            prossimo_btn
        ], alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(main)