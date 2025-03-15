def bubble_sort(l, crescente = True):
    for i in range(1, len(l)):
        for j in range(0, len(l) - i):
            if crescente and l[j] > l[j + 1] or not(crescente) and l[j] < l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]

def insertion_sort(l, cresente = True):
    for i in range(1, len(l)):
        j = i
        if cresente:
            while j > 0 and l[j - 1] > l[j]:
                l[j], l[j - 1] = l[j - 1], l[j]
                j -= 1
        else:
            while j > 0 and l[j - 1] < l[j]:
                l[j], l[j - 1] = l[j - 1], l[j]
                j -= 1
