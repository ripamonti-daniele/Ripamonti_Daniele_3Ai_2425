def filtro(p, mostra_dir, estensioni):
    from os import path, listdir

    if path.exists(p):

        elementi = []
        f = listdir(p)

        if mostra_dir == True:
            for i in f:
                perc = path.join(p, i)
                if path.isdir(perc):
                    elementi.append(i)

        if len(estensioni) > 0:
            for i in estensioni:
                for j in f:
                    if j.endswith(i):
                        elementi.append(j)

        else:
            for i in f:
                elementi.append(i)

        return elementi

    else:
        return FileNotFoundError("errore: percorso non valido")
