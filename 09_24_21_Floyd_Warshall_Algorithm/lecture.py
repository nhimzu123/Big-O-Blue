"""
- Floyd Warshall Algorithm: Thuật toán tìm đường đi ngắn nhất giữa tất cả các cặp đỉnh trong đồ thị có hướng,
 có trọng số (trọng số có thể dương hoặc âm). Không chạy được với đồ thị tồn tại chu trình âm.
- Độ phức tạp: O(V**3)
"""


def print_path(path, s, f):
    if s == f:
        print(f, end=' ')
        return
    if path[s][f] == -1:
        print('No path', end=' ')
        return
    print_path(path, s, path[s][f])
    print(f, end=' ')


def print_solution(path, dist, v):
    for i in range(v):
        for j in range(v):
            if i != j:
                print('{}->{}'.format(i, j), end=' ')
                print_path(path, i, j)
                print()

                if path[i][j] != -1:
                    print('Total length: {}'.format(dist[i][j]))


def floyd_warshall(graph, dist, path, v):
    for i in range(v):
        for j in range(v):
            dist[i][j] = graph[i][j]
            if graph[i][j] != INF and i != j:
                path[i][j] = i
            else:
                path[i][j] = -1

    for k in range(v):
        for i in range(v):
            if dist[i][k] == INF:
                continue
            for j in range(v):
                if dist[k][j] != INF and dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = path[k][j]
        # Check negative cycle
    for i in range(v):
        if dist[i][i] < 0:
            return False

    return True


if __name__ == '__main__':
    INF = int(1e9)
    V = int(input())

    graph = [[0 for _ in range(V)] for _ in range(V)]
    dist = [[0 for _ in range(V)] for _ in range(V)]
    path = [[0 for _ in range(V)] for _ in range(V)]

    for i in range(V):
        line = list(map(int, input().split()))
        for j in range(V):
            graph[i][j] = INF if line[j] == 0 and i != j else line[j]

    res = floyd_warshall(graph, dist, path, V)

    if res:
        print_solution(path, dist, V)
    else:
        print('Graph contains negative weight cycle')
