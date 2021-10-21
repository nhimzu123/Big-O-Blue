"""
SPOJ: Cobbled Streets
"""
from queue import PriorityQueue


class Node:
    def __init__(self, index, distance):
        self.idx = index
        self.dist = distance

    def __lt__(self, other):
        return self.dist <= other.dist


def prims(graph, src):
    pq = PriorityQueue()
    pq.put(Node(src, 0))
    dist = [INF for _ in range(n)]
    visited = [False for _ in range(n)]
    dist[src] = 0
    cost = 0

    while not pq.empty():
        top = pq.get()
        u = top.idx
        visited[u] = True

        for neighbor in graph[u]:
            v = neighbor.idx
            w = neighbor.dist
            if not visited[v] and w < dist[v]:
                dist[v] = w
                pq.put(neighbor)

    for i in range(n):
        cost += dist[i]
    return cost


if __name__ == '__main__':
    INF = 10 ** 9
    for _ in range(int(input())):
        p = int(input())
        n = int(input())
        graph = [[] for _ in range(n)]

        for _ in range(int(input())):
            d = list(map(int, input().split()))
            graph[d[0] - 1].append(Node(d[1] - 1, d[2]))
            graph[d[1] - 1].append(Node(d[0] - 1, d[2]))

        print(prims(graph, 0) * p)
