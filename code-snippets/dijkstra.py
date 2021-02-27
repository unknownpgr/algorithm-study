# https://justkode.kr/algorithm/python-dijkstra

import heapq


def dijkstra(edges, start):
    dist = {node: float('inf') for node in edges}
    dist[start] = 0
    node_from = {start: start}
    queue = []
    heapq.heappush(queue, [dist[start], start])
    while len(queue) > 0:
        current_distance, current_destination = heapq.heappop(queue)
        if dist[current_destination] < current_distance:
            continue
        for new_destination, new_distance in edges[current_destination].items():
            distance = current_distance + new_distance
            if distance < dist[new_destination]:
                dist[new_destination] = distance
                node_from[new_destination] = current_destination
                heapq.heappush(queue, [distance, new_destination])
    return dist, node_from


graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

print(dijkstra(graph, 'A'))
