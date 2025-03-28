import flet as ft 

def main(page: ft.Page):
    page.title = "Primo programma" #titolo finestra
    page.vertical_alignment = ft.MainAxisAlignment.CENTER #allinea al centro della finestra il contatore

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100) #controllo

    c1 = ft.Checkbox(label="Psx", value=False)
    c2 = ft.Checkbox(label="Xbox", value=False)
    c3 = ft.Checkbox(label="Switch", value=False)

    label1 = ft.Text("", color="#0000ff", size=15)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        txt_number.update()
        #oppure page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        txt_number.update()

    def b1_clicked(e):
        txt_number.value = "ciao"
        txt_number.update()

    def console_clicked(e):
        stringa = "Hai scelto: "
        if c1.value:
            stringa += "Psx, "
        if c2.value:
            stringa += "Xbox, "
        if c3.value:
            stringa += "Switch, "

        stringa = stringa[:-2]
        label1.value = stringa
        label1.update()

    page.add(
        ft.Row(
            [
                ft.TextButton(text="Premi qui", on_click=b1_clicked), # bottone
                # ft.TextButton(text="Disabled button", disabled=True), # bottone disabilitato
                ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.Icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),

        ft.Row(
            [
                ft.Text("Scegli le tua console:", color="#ff0000", size=20, bgcolor="#abcdef")
            ],
            alignment=ft.MainAxisAlignment.START
        ),

        ft.Row(
            [
                c1, c2, c3
            ],
            alignment=ft.MainAxisAlignment.START
        ),

        ft.Row(
            [
                ft.TextButton("Conferma scelta", icon="agriculture", on_click=console_clicked, icon_color="green400"),
                label1
            ],
            alignment=ft.MainAxisAlignment.START

        )

    )

ft.app(main)