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
            numero=str(numero)
            corazones.append(f"{numero}{tipo}")
        elif tipo == 't':
            numero=str(numero)
            treboles.append(f"{numero}{tipo}")
        elif tipo == 'd':
            numero=str(numero)
            diamantes.append(f"{numero}{tipo}")
        elif tipo == 'p':
            numero=str(numero)
            picas.append(f"{numero}{tipo}")

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
    for i in range(1, n):
        key = lista[i]
        j = i - 1
        
        # Extrae número y palo de la carta 'key'
        key_num = int(key[:-1])   # número (ej: "10c" -> 10)
        key_palo = key[-1]        # palo (ej: "10c" -> "c")

        # Comparación dentro del while
        while j >= 0:
            # Extrae número y palo de la carta en lista[j]
            j_num = int(lista[j][:-1])
            j_palo = lista[j][-1]
            
            # Compara primero por número y luego por palo
            if key_num < j_num or (key_num == j_num and key_palo < j_palo):
                lista[j + 1] = lista[j]
                j -= 1
            else:
                break
        
        lista[j + 1] = key

    return lista