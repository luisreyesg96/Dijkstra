import sys

# Función para encontrar el índice del nodo con la distancia más corta en el conjunto de nodos no visitados
def encontrar_nodo_menor_distancia(distancias, visitados):
    min_distancia = sys.maxsize
    min_indice = -1
    for i in range(len(distancias)):
        if distancias[i] < min_distancia and not visitados[i]:
            min_distancia = distancias[i]
            min_indice = i
    return min_indice

# Implementación del algoritmo de Dijkstra
def dijkstra(grafo, nodo_inicio):
    num_nodos = len(grafo)
    distancias = [sys.maxsize] * num_nodos  # Distancias iniciales al infinito
    distancias[nodo_inicio] = 0  # La distancia al nodo de inicio es 0
    visitados = [False] * num_nodos

    for _ in range(num_nodos):
        nodo_actual = encontrar_nodo_menor_distancia(distancias, visitados)
        visitados[nodo_actual] = True
        for j in range(num_nodos):
            if grafo[nodo_actual][j] > 0 and not visitados[j] and distancias[j] > distancias[nodo_actual] + grafo[nodo_actual][j]:
                distancias[j] = distancias[nodo_actual] + grafo[nodo_actual][j]

    return distancias

# Grafo de ejemplo con 10 nodos y sus respectivas conexiones y pesos
grafo = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2, 0],
    [0, 0, 7, 0, 9, 14, 0, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6, 0],
    [8, 11, 0, 0, 0, 0, 1, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 6, 7, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
]

nodo_inicio = 0  # Nodo de inicio para el algoritmo de Dijkstra

distancias = dijkstra(grafo, nodo_inicio)

# Imprimir las distancias más cortas desde el nodo de inicio a los demás nodos
for i in range(len(distancias)):
    print(f"Distancia desde el nodo {nodo_inicio} hasta el nodo {i}: {distancias[i]}")
