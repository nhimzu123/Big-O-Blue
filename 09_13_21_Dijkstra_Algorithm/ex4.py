"""
SPOJ: Traffic Network
"""

from queue import PriorityQueue


class Node:
    def __init__(self, p_id, distance):
        self.p_id = p_id
        self.dist = distance

    def __lt__(self, other):
        return self.dist <= other.dist


def dijkstra(s):
    pq = PriorityQueue()
    pq.put(Node(s, 0))
    dist[s] = 0

    while not pq.empty():
        top = pq.get()
        u = top.p_id
        w = top.dist

        if dist[u] != w:
            continue

        for neighbor in graph[u]:
            if w + neighbor.dist < dist[neighbor.p_id]:
                dist[neighbor.p_id] = w + neighbor.dist
                pq.put(Node(neighbor.p_id, dist[neighbor.p_id]))
                path[neighbor.p_id] = u


if __name__ == '__main__':
    INF = int(1e9)
    for i in range(int(input())):
        n, m, k, s, t = map(int, input().split())
        graph = [[] for _ in range(n + 1)]

        for _ in range(m):
            d = list(map(int, input().split()))
            graph[d[0]].append(Node(d[1], d[2]))

        min_dist = INF
        for _ in range(k):
            path = [-1 for _ in range(n + 1)]
            dist = [INF for _ in range(n + 1)]

            d = list(map(int, input().split()))
            graph[d[0]].append(Node(d[1], d[2]))
            graph[d[1]].append(Node(d[0], d[2]))
            dijkstra(s)
            if dist[t] < min_dist:
                min_dist = dist[t]
            graph[d[0]].pop()
            graph[d[1]].pop()

        print(min_dist if min_dist != INF else -1)
