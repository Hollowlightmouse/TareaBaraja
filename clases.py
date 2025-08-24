#Llamado de clase 
import random  

# Función que genera un mazo estándar de 52 cartas y lo baraja
def genera_mazo():  
    # Tipos de cartas: c = corazones, t = tréboles, d = diamantes, p = picas
    tipos_cartas = ['c', 't', 'd', 'p']
    
    # Valores de las cartas del 1 al 13 (1 = As, 11 = J, 12 = Q, 13 = K)
    valores = list(range(1, 14))
    
    # Lista que contendrá todas las combinaciones de valor+tipo
    mazo = []
    
    # Genera todas las cartas posibles (ejemplo: "1c", "12d", "13p")
    for tipo in tipos_cartas:
        for valor in valores:
            mazo.append(f"{valor}{tipo}") 
    
    # Mezcla el mazo en su lugar (modifica la lista directamente)
    random.shuffle(mazo)
    
    # Devuelve el mazo ya barajado
    return mazo
    
def organizar_mazo(cartas):
    # Listas para separar las cartas según su tipo
    corazones = []
    treboles = []
    diamantes = []
    picas = []

    # Recorremos todas las cartas del mazo recibido
    for carta in cartas:
        numero = int(carta[:-1])   # Extrae el número (todo menos la última letra)
        tipo = carta[-1]           # Extrae el tipo (última letra)

        # Clasifica la carta según su tipo y la guarda en la lista correspondiente
        if tipo == 'c':
            corazones.append(numero)
        elif tipo == 't':
            treboles.append(numero)
        elif tipo == 'd':
            diamantes.append(numero)
        elif tipo == 'p':
            picas.append(numero)

    # Devuelve las listas separadas por tipo
    return corazones, treboles, diamantes, picas


# def selection_sort(lista):
#     n = len(lista)
#     # Recorre la lista desde la posición 0 hasta la última
#     for i in range(n):
#         # Supone que el elemento actual (i) es el mínimo
#         min_idx = i
#         # Busca un valor menor en el resto de la lista
#         for j in range(i+1, n):
#             if lista[j] < lista[min_idx]:
#                 min_idx = j
#         # Intercambia el mínimo encontrado con el actual
#         lista[i], lista[min_idx] = lista[min_idx], lista[i]
#     # Devuelve la lista ya ordenada
#     return lista


def insertion_sort(lista):
    n = len(lista)
    # Recorre la lista a partir del segundo elemento
    for i in range(1, n):
        key = lista[i]       # Elemento actual a insertar en la parte ordenada
        j = i - 1
        # Desplaza hacia la derecha los elementos mayores que 'key'
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        # Inserta 'key' en la posición correcta
        lista[j + 1] = key
    # Devuelve la lista ordenada
    return lista
