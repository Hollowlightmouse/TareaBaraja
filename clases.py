import random  

def genera_mazo():  
    palos = ['c', 't', 'd', 'p']
    valores = list(range(1, 14))
    mazo = []
    for palo in palos:
        for valor in valores:
            mazo.append(f"{valor}{palo}") 
    random.shuffle(mazo)
    return mazo

mazo_desordenado = genera_mazo()
print(mazo_desordenado)
print(f"Número de cartas en el mazo: {len(mazo_desordenado)}")


def seleccion(mazo):
    orden_palos = {'c': 0, 't': 1, 'd': 2, 'p': 3}
    n = len(mazo)
    for i in range(n - 1):
        min_index = i
        valor_min = int(mazo[min_index][:-1])
        palo_min = mazo[min_index][-1]
        
        for j in range(i + 1, n):
            valor_j = int(mazo[j][:-1])
            palo_j = mazo[j][-1]
            if (valor_j < valor_min) or (valor_j == valor_min and orden_palos[palo_j] < orden_palos[palo_min]):
                min_index = j
                valor_min = valor_j
                palo_min = palo_j
        
        # Intercambiar
        mazo[i], mazo[min_index] = mazo[min_index], mazo[i]
    return mazo
