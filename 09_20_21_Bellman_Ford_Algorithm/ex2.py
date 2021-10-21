"""
LightOj: Extended Traffic
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

    for i in range(1,n):
        for j in range(m):
            u,v,w = graph[j].source, graph[j].target, graph[j].weight
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = -INF

    for i in range(m):
        u, v, w = graph[i].source, graph[i].target, graph[i].weight
        if dist[u] != INF and dist[u] + w < dist[v]:
            return False

    return True


if __name__ == '__main__':
    INF = int(1e9)
    for case in range(int(input())):
        input()
        n = int(input())

        graph = []
        dist = [INF for _ in range(n + 1)]
        path = [-1 for _ in range(n + 1)]

        cost = list(map(int, input().split()))
        m = int(input())
        for edge in range(m):
            u, v = map(int, input().split())
            graph.append(Edge(u, v, (cost[v - 1] - cost[u - 1]) ** 3))

        res = bellman_ford(1)

        print("Case {}:".format(case + 1))

        for _ in range(int(input())):
            dest = int(input())
            if dist[dest] < 3:
                print("?")
            else:
                print(dist[dest])
