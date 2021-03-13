# https://justkode.kr/algorithm/python-dijkstra

import heapq


def dijkstra(edges, start):
    dist = {node: float('inf') for node in edges}
    dist[start] = 0
    node_from = {start: start}
    queue = []

    heapq.heappush(queue, [dist[start], start])
    while len(queue) > 0:
        curr_dist, curr_dest = heapq.heappop(queue)

        if dist[curr_dest] < curr_dist:
            continue

        for new_dest, new_dist in edges[curr_dest].items():
            distance = curr_dist + new_dist

            if distance < dist[new_dest]:
                dist[new_dest] = distance
                node_from[new_dest] = curr_dest
                heapq.heappush(queue, [distance, new_dest])

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
