"""
Dijkstra Algorithm: Thuật toán tìm đường đi ngắn nhắt trên đồ thị có trọng số, từ một
đỉnh đến các đỉnh còn lại.
Độ phức tạp O = E*logV
"""

from queue import PriorityQueue


class Node:
    """
    point_id: point's name
    """
    def __init__(self, p_id, dist):
        self.p_id = p_id
        self.dist = dist

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
    MAX = 100
    INF = int(1e9)
    n = int(input())

    # Starting point s=0 - Searching point t=4
    s, t = 0, 4

    graph = [[] for i in range(n + 5)]
    dist = [INF for i in range(n + 5)]
    path = [-1 for i in range(n + 5)]

    for i in range(n):
        d = list(map(int, input().split()))
        for j in range(n):
            if d[j] > 0:
                graph[i].append(Node(j, d[j]))

    dijkstra(s)

    answer = dist[t]
    print(answer)
