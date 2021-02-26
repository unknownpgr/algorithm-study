def floyd_warshall(dist):
    '''
    dist should be a 2D array that contains distance between two vertices.
    dist[start][end] = dist between start and end.
    if there is no edge connecting start and end vertices, dist[start][end] should be infinity.

    it will return the minimum distacne between all two vertices.
    '''

    l = len(dist)
    for k in range(l):
        for i in range(l):
            for j in range(l):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

    return dist
