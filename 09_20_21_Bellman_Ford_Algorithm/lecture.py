"""
- Bellman-Ford Algorithm: Thuật toán tìm đường đi có chi phí nhỏ nhất từ một đỉnh đến tất cả các đỉnh còn lại trong
đồ thị có hướng hoặc vô hướng, có trọng số (trọng số có thể dương hoặc âm)
- Độ phức tạp: O(E*V)
"""


class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight


def bellman_ford(s):
    dist[s] = 0

    for i in range(1, n):
        for j in range(e):
            u, v, w = graph[j].source, graph[j].target, graph[j].weight
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                path[v] = u

    # Kiểm tra có tồn tại chu trình âm vô hạn
    for i in range(e):
        u, v, w = graph[i].source, graph[i].target, graph[i].weight
        if dist[u] != INF and dist[u] + w < dist[v]:
            return False
    return True


if __name__ == '__main__':
    INF = int(1e9)
    n, e = map(int, input().split())

    graph = []
    dist = [INF for _ in range(n)]
    path = [-1 for _ in range(n)]

    for _ in range(e):
        s, t, w = map(int, input().split())
        graph.append(Edge(s, t, w))

    s, t = 0, 2

    res = bellman_ford(0)
    print(dist)
    print(path)
    if not res:
        print("Graph contains negative weight cycle")
    else:
        print(dist[t])
