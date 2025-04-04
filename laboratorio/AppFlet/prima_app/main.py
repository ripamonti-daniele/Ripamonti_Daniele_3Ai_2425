import datetime
import flet as ft

def main(page: ft.Page):
    #gestione eventi
    def bt_nome_click(e):
        if tb_nome.value == "":
            page.open(dialog)

        else:
            lb_nome.value = f"Ciao {tb_nome.value}, benvenuto in 3Ai"
            lb_nome.visible = True
            lb_nome.update()

    def data_change(e):
        lb_data.value = f"Hai scelto la data {e.control.value.strftime('%d-%m-%Y')}"
        lb_data.visible = True
        lb_data.update()

    #controlli
    #https://gallery.flet.dev/icons-browser/
    tb_nome = ft.TextField(label="Inserire il nome", icon=ft.Icons.SPORTS_VOLLEYBALL)
    bt_nome = ft.ElevatedButton("conferma nome", on_click=bt_nome_click)
    lb_nome = ft.Text("", visible=False)
    bt_data = ft.FilledButton("Scegli una data", icon="EDIT_CALENDAR", on_click=lambda e: page.open(datepicker))
    lb_data = ft.Text("", visible=False)

    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Attenzione", color="red"),
        content=ft.Text("Mi raccomando, compila per bene\ntutti i campi partendo dal nome"),
        actions=[
            ft.TextButton("Ok", on_click=lambda e: page.close(dialog))
        ]
    )

    datepicker = ft.DatePicker(
        first_date=datetime.datetime(2024, 9, 12),
        last_date=datetime.datetime(2025, 6, 7),
        on_change=data_change
    )
    
    #layout applicazione
    view = ft.Column([
        ft.Row([ft.Text("Inserimento dati", size=18)]),
        ft.Row([tb_nome, bt_nome]),
        ft.Row([lb_nome]),
        ft.Row([bt_data, lb_data]),
    ])

    page.title = "Applicazione uso controlli"
    page.theme_mode = ft.ThemeMode.LIGHT

    page.add(view)

ft.app(main)