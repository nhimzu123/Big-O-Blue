"""
SPOJ: Minimum Spanning Tree
"""

from queue import PriorityQueue


class Node:
    def __init__(self, p_id, distance):
        self.p_id = p_id
        self.dist = distance

    def __lt__(self, other):
        return self.dist <= other.dist


def prims(src):
    pq = PriorityQueue()
    pq.put(Node(src, 0))
    dist[src] = 0

    while not pq.empty():
        top = pq.get()
        u = top.p_id
        visited[u] = True

        for neigbor in graph[u]:
            v = neigbor.p_id
            w = neigbor.dist

            if not visited[v] and w < dist[v]:
                dist[v] = w
                pq.put(neigbor)
                path[v] = u


def print_mst():
    ans = 0
    for i in range(1, n + 1):
        if path[i] == -1:
            continue
        ans += dist[i]
    return ans


if __name__ == '__main__':
    INF = 10 ** 9

    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        d = list(map(int, input().split()))
        graph[d[0]].append(Node(d[1], d[2]))
        graph[d[1]].append(Node(d[0], d[2]))

    visited = [False for _ in range(n + 1)]
    dist = [INF for _ in range(n + 1)]
    path = [-1 for _ in range(n + 1)]

    prims(1)
    print(print_mst())
