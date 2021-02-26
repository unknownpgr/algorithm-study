import sys


def read_int_array():
    return list(map(int, sys.stdin.readline().split()))


def read_int_array_2d(n):
    array = []
    for _ in range(n):
        array.append(list(map(int, sys.stdin.readline().split())))
    return array


def edges_to_dist(n, edges):
    '''
    edges should be an array of the tuples (or arrays) that describe edges in the form of (start,end,dist).
    '''
    inf = float('inf')
    dist = [[inf]*n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for s, e, d in edges:
        dist[s][e] = min(dist[s][e], d)
    return dist
