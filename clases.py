import random  

def genera_mazo():  
    palos = ['c', 't', 'd', 'p']
    valores = list(range(1, 14))
    mazo = []
    for mazo_nuevo in palos:
        for valor in valores:
            mazo.append(f"{valor}{mazo_nuevo}") 
    random.shuffle(mazo)
    return mazo

def organizar_mazo(cartas):
    corazones = []
    treboles = []
    diamantes = []
    picas = []

    for carta in cartas:
        numero = int(carta[:-1])  # Todo menos la última letra
        mazo_nuevo = carta[-1]          # Última letra

        if mazo_nuevo == 'c':
            corazones.append(numero)
        elif mazo_nuevo == 't':
            treboles.append(numero)
        elif mazo_nuevo == 'd':
            diamantes.append(numero)
        elif mazo_nuevo == 'p':
            picas.append(numero)

    return corazones, treboles, diamantes, picas


def selection_sort(lista):
    n = len(lista)
    # Recorre la lista de 0 a n-1
    for i in range(n):
        # Encuentra el índice del elemento mínimo en la parte no ordenada
        min_idx = i
        for j in range(i+1, n):
            # Compara el elemento actual con el mínimo encontrado
            if lista[j] < lista[min_idx]:
                min_idx = j
        # Intercambia el elemento mínimo con el primer elemento de la parte no ordenada
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

def insertion_sort(lista):
    n = len(lista)
    # Recorre la lista desde el segundo elemento
    for i in range(1, n):
        key = lista[i]
        j = i - 1
        # Mueve los elementos de la lista ordenada que son mayores que la 'key'
        # a una posición adelante de su posición actual
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]

            j -= 1
        lista[j + 1] = key
    return lista