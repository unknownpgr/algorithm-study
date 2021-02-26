import sys

'''
Union-Find is an algorithm for searching and modifying execlusive sets.
In this algorithm, Weighted Union Find is not implemented.
'''


'''
array is an array of nodes in the from of [index of parant, depth of node].
'''
array = []


def add_node(parent):
    if parent < 0:
        parent = len(array)
    array.append([parent, 1])


def init_array(n):
    global array
    array = []
    for i in range(n):
        array.append([i, 1])


def find(x):
    '''
    find the root node of given node
    '''
    if array[x][0] == x:
        return x
    y = find(array[x][0])
    array[x][0] = y
    return y


def union(x, y):
    '''
    union two exclusive sets
    '''
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
