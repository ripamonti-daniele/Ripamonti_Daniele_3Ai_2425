# Realizzare un programma python flet in grado di permettere ad uno studente di prenotare una interrogazione.
# il programma richiede:
# nome, cognome, classe, materia, data, ora
# effettuare gli opportuni controlli sui dati inseriti e visualizzare un messaggio di riepilogo.

import flet as ft

def main(page: ft.Page):
    page.title = "Applicazione uso controlli"
    # ft.VerticalAlignment = ft.MainAxisAlignment.START

    #funzioni
    def controllo_nome(e):
        if len(e.data) > 0 and not(e.data.isalpha()):
            txt_nome.label = "Nome - Caratteri non validi"
            txt_nome.border_color = "red"
            txt_nome.label_style=ft.TextStyle(color=ft.colors.RED)
            
        elif len(e.data) < 2 and len(e.data) > 0:
            txt_nome.label = "Nome - Troppo corto"
            txt_nome.border_color = "red"
            txt_nome.label_style=ft.TextStyle(color=ft.colors.RED)
        
        elif len(e.data) > 20:
            txt_nome.label = "Nome - Troppo lungo"
            txt_nome.border_color = "red"
            txt_nome.label_style=ft.TextStyle(color=ft.colors.RED)
            
        else:
            txt_nome.label = "Nome"
            txt_nome.border_color = ""
            txt_nome.label_style=ft.TextStyle(color="")
            
        txt_nome.update()

    def controllo_cognome(e):
        if len(e.data) > 0 and not(e.data.isalpha()):
            txt_cognome.label = "Cognome - Caratteri non validi"
            txt_cognome.border_color = "red"
            txt_cognome.label_style=ft.TextStyle(color=ft.colors.RED)
            
        elif len(e.data) < 2 and len(e.data) > 0:
            txt_cognome.label = "Cognome - Troppo corto"
            txt_cognome.border_color = "red"
            txt_cognome.label_style=ft.TextStyle(color=ft.colors.RED)
        
        elif len(e.data) > 20:
            txt_cognome.label = "Cognome - Troppo lungo"
            txt_cognome.border_color = "red"
            txt_cognome.label_style=ft.TextStyle(color=ft.colors.RED)
            
        else:
            txt_cognome.label = "Cognome"
            txt_cognome.border_color = ""
            txt_cognome.label_style=ft.TextStyle(color="")
            
        txt_cognome.update()

    #elementi
    txt_nome = ft.TextField(label="Nome", on_change=controllo_nome)
    txt_cognome = ft.TextField(label="Cognome", on_change=controllo_cognome)

    #messa a schermo
    page.add(
        ft.Column(
            [
                ft.Row(
                    [
                        txt_nome, 
                        txt_cognome,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(main)
