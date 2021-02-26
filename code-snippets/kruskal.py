'''
The Kruskal algorithm is an algorithm for findings the minimum spanning tree.
Minimum spanning tree means a subgraph of a graph which is a tree and has minimum length.
Kruscal algorithm is a greedy algorithm that finds actually optimal solution.
It uses union-find algorithm internally.
'''

array = []


def init_array(n):
    global array
    array = []
    for i in range(n):
        array.append([i, 1])


def find(x):
    if array[x][0] == x:
        return x
    y = find(array[x][0])
    array[x][0] = y
    return y


def union(x, y):
    x = find(x)
    y = find(y)
    if (x == y):
        return
    if array[x][1] > array[y][1]:
        array[y][0] = x
        array[x][1] += array[y][1]
    else:
        array[x][0] = y
        array[y][1] += array[x][1]


def kruskal(n, edges):
    '''
    edges should be an array of the tuples (or arrays) that describe edges in the form of (start,end,dist).
    '''

    init_array(n)
    edges = sorted(edges, key=lambda x: -x[2])

    mst = []

    while len(edges) > 0:
        edge = edges.pop()
        start, end, _ = edge
        if find(start) != find(end):
            mst.append(edge)
            union(start, end)

    return mst
