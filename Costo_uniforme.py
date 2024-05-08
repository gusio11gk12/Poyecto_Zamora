def dijkstra(Grafo, salida):
    dist, prev = {}, {}

    for vertice in Grafo:
        dist[vertice] = float("inf")
        prev[vertice] = None
    dist[salida] = 0

    Q = set(Grafo.keys())

    while Q:
        u = min(Q, key=dist.get)
        Q.remove(u)

        for vecino, peso in Grafo[u].items():
            alt = dist[u] + peso
            if alt < dist[vecino]:
                dist[vecino] = alt
                prev[vecino] = u

    return prev

def reconstruir_camino(previos, nodo):
    camino = []
    while nodo is not None:
        camino.insert(0, nodo)
        nodo = previos[nodo]
    return camino

# Definición de las conexiones del grafo
conexiones = {
    'EDO.MEX': {'SLP': 513, 'CDMX': 125},
    'PUEBLA': {'SLP': 514},
    'CDMX': {'MICHOACAN': 491, 'SLP': 423, 'EDO.MEX': 125},
    'MICHOACAN': {'SONORA': 346, 'SLP': 355, 'MONTERREY': 309, 'CDMX': 491},
    'SLP': {'QRO': 203, 'PUEBLA': 514, 'EDO.MEX': 513, 'SONORA': 603, 'GUADALAJARA': 437, 'CDMX': 423,
            'MICHOACAN': 355, 'MONTERREY': 313, 'HIDALGO': 599},
    'QRO': {'SLP': 203, 'HIDALGO': 390},
    'HIDALGO': {'QRO': 390, 'SLP': 599},
    'MONTERREY': {'SLP': 313, 'SONORA': 296, 'GUADALAJARA': 394, 'MICHOACAN': 309},
    'SONORA': {'MONTERREY': 296, 'SLP': 603, 'MICHOACAN': 346},
    'GUADALAJARA': {'MONTERREY': 394, 'SLP': 437}
}

salida = 'EDO.MEX'
nodo_destino = 'HIDALGO'
previos = dijkstra(conexiones, salida)
camino = reconstruir_camino(previos, nodo_destino)
print(f"Camino más corto desde el nodo {salida} hasta el nodo {nodo_destino}: {camino}")
