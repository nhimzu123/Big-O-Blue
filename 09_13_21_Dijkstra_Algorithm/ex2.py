"""
SPOJ: Mice and Maze
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
    n = int(input())

    graph = [[] for i in range(n + 1)]

    f_point = int(input())
    time = int(input())

    for i in range(int(input())):
        d = list(map(int, input().split()))
        graph[d[0]].append(Node(d[1], d[2]))

    count = 0
    for i in range(1, n + 1):
        dist = [INF for _ in range(n + 1)]
        path = [-1 for _ in range(n + 1)]
        dijkstra(i)
        if dist[f_point] <= time:
            count += 1

    print(count)
