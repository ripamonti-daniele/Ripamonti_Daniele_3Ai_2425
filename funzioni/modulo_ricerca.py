def ricerca_lineare_base(lista, n):
    esito = False
    for i in lista:
        if i == n:
            esito = True
    return esito

def ricerca_lineare_migliorata(lista, n):
    for i in lista:
        if i == n:
            return True
    return False
