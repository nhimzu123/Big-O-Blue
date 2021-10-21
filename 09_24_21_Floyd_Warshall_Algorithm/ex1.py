"""
SPOJ: Possible Friends
"""

INF = 10 ** 9


def floyd_warshall():
    for k in range(M):
        for i in range(M):
            for j in range(M):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


T = int(input())

for _ in range(T):
    s = input()
    M = len(s)
    dist = [[INF] * M for i in range(M)]
    matrix = []

    for i in range(M):
        if i == 0:
            matrix.append(s)
        else:
            matrix.append(input())

        for j in range(M):
            if matrix[i][j] == 'Y':
                dist[i][j] = 1
            elif i == j:
                dist[i][j] = 0

    floyd_warshall()
    nfriends, index = 0, 0

    for i in range(M):
        count = 0

        for j in range(M):
            if dist[i][j] == 2:
                count += 1

        if count > nfriends:
            nfriends = count
            index = i

    print(index, nfriends)
