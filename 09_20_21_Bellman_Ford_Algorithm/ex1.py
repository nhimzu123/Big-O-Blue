"""
UVA: Wormholes
"""


class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight


def bellman_ford(s):
    dist[s] = 0

    for i in range(1, n):
        for j in range(m):
            u, v, w = graph[j].source, graph[j].target, graph[j].weight
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                path[v] = u

    for i in range(m):
        u, v, w = graph[i].source, graph[i].target, graph[i].weight
        if dist[u] != INF and dist[u] + w < dist[v]:
            return False

    return True


if __name__ == '__main__':
    INF = int(1e9)

    for _ in range(int(input())):
        n, m = map(int, input().split())

        graph = []
        dist = [INF for _ in range(n)]
        path = [-1 for _ in range(n)]

        for _ in range(m):
            s, t, w = map(int, input().split())
            graph.append(Edge(s, t, w))
        s = 0
        res = bellman_ford(s)
        if not res:
            print('possible')
        else:
            print("not possible")
