import clases  # Importamos el módulo "clases" que contiene las funciones necesarias

# Generamos un mazo de cartas utilizando la función definida en "clases"
Mazo = clases.genera_mazo()
print(f"Mazo generado: {Mazo}")  # Mostramos el mazo completo
print(f"numero de cartas en el mazo {len(Mazo)}")  # Mostramos la cantidad total de cartas

# Separamos el mazo en 4 listas, una por cada palo (corazones, tréboles, diamantes y picas)
corazones, treboles, diamantes, picas = clases.organizar_mazo(Mazo)
print("mazo separado")  
print(f"Corazones: {corazones}")
print(f"Treboles: {treboles}")
print(f"Diamantes: {diamantes}")
print(f"Picas: {picas}")

# Ordenamos cada palo individualmente utilizando el método de ordenamiento por inserción
corazones = clases.insertion_sort(corazones)
treboles = clases.insertion_sort(treboles)
diamantes = clases.insertion_sort(diamantes)
picas = clases.insertion_sort(picas)

print("mazo organizado")  
print(f"Corazones: {corazones}")   # Muestra los corazones ya ordenados
print(f"Treboles: {treboles}")     # Muestra los tréboles ya ordenados
print(f"Diamantes: {diamantes}")   # Muestra los diamantes ya ordenados
print(f"Picas: {picas}")           # Muestra las picas ya ordenadas
