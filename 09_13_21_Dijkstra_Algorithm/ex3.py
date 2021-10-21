"""
SPOJ: The Shortest Path
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
        city = {}
        n = int(input())
        graph = [[] for _ in range(n + 1)]

        for _ in range(1, n + 1):
            city[input()] = _
            for j in range(int(input())):
                name, z = map(int, input().split())
                graph[_].append(Node(name, z))

        for _ in range(int(input())):
            name1, name2 = input().split()
            path = [-1 for _ in range(n + 1)]
            dist = [INF for _ in range(n + 1)]
            dijkstra(city[name1])
            print(dist[city[name2]])
        input()
