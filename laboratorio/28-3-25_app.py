# app che chiede nome e cognome, la classe, gli sport, il sesso, anno di nascita
# per l'iscrizione al campionato di fine anno

# ci si può iscrivere a un solo sprt tra calcio, basket, ping pong (anche misti) e atletica
# console preferita tra psx, xbox, switch

# effettua gli eventuali controlli sui dati inseriti e visualizza un riepilogo delle informazioni collezionate

import flet as ft

def main(page: ft.Page):
    page.title = "Inscrizione Tornei Fine Anno"
    ft.VerticalAlignment = ft.MainAxisAlignment.START

    txt_nome = ft.TextField(label="Nome")
    txt_cognome = ft.TextField(label="Cognome")
    txt_anno = ft.TextField(label="Anno di nascita")
    scelta_sesso = ft.RadioGroup(content=ft.Column(
        [
        ft.Radio(value="Uomo", label="Uomo"),
        ft.Radio(value="Donna", label="Donna"),
        ]))

    # searchbar classe

    scelta_sport = ft.RadioGroup(content=ft.Column(
        [
        ft.Radio(value="Calcio", label="Calcio"),
        ft.Radio(value="Basket", label="Basket"),
        ft.Radio(value="Ping Pong", label="Ping Pong"),
        ft.Radio(value="Atletica", label="Atletica"),
        ]))

    scelta_console = ft.RadioGroup(content=ft.Column(
        [
        ft.Radio(value="PlayStation", label="PlayStation"),
        ft.Radio(value="Xbox", label="Xbox"),
        ft.Radio(value="Switch", label="Switch"),
        ]))




    page.add(
        ft.Row(
            [
                ft.Text("Iscrizione Tornei Fine Anno", size=40)
            ],
            alignment=ft.MainAxisAlignment.START
        ),

        ft.Row(
            [
                ft.Column(
                    [
                        txt_nome
                    ], 
                    alignment=ft.MainAxisAlignment.START
                ),

                ft.Column(
                    [
                        txt_cognome
                    ], 
                    alignment=ft.MainAxisAlignment.START
                ),

                ft.Column(
                    [
                        txt_anno
                    ], 
                    alignment=ft.MainAxisAlignment.START
                ),

                ft.Column(
                    [
                        ft.Text("Sesso:",size=20),
                        scelta_sesso
                    ], 
                    alignment=ft.MainAxisAlignment.START
                ),
            ], 
            alignment=ft.MainAxisAlignment.START
        ),
        
        ft.Row(
            [
                ft.Column(
                    [
                        # searchbar classe
                    ], 
                    alignment=ft.MainAxisAlignment.START
                ),

                ft.Column(
                    [
                        ft.Text("Torneo al quale vuoi partecipare", size=20),
                        scelta_sport
                    ], 
                    alignment=ft.MainAxisAlignment.START
                ),

                ft.Column(
                    [
                        ft.Text("Scegli la tua console preferita", size=20),
                        scelta_console
                    ], 
                    alignment=ft.MainAxisAlignment.START
                ),

                ft.Column(
                    [
                        
                    ], 
                    alignment=ft.MainAxisAlignment.START
                ),
            ], 
            alignment=ft.MainAxisAlignment.START
        )
    )

ft.app(main)