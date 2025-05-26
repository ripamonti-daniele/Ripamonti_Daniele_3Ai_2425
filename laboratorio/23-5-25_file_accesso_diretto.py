# programma che permette di vedere l'aforisma del giorno
# sezione con cui si può aggiungere qualche nuovo aforisma

import flet as ft 

def main(page: ft.Page):
    page.title = "Aforismi"
    
    page.add()

ft.app(main)