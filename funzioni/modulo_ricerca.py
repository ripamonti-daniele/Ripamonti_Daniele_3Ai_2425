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

def ricerca_binaria(l, n):
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            print("lista non in ordine")
            return False
    
    i = (len(l) // 2)
    j = i

    while True:
        j = j // 2
        if l[i] == n:
            return i
        
        elif i == 0 or i == len(l) -1:
            return False
        
        elif l[i] < n and l[i + 1] > n:
            return False
        
        else:
            k = i
            if n < l[i]:
                i -= j
                if i == k:
                    i -= 1
            else:
                i += j
                if i == k:
                    i += 1
