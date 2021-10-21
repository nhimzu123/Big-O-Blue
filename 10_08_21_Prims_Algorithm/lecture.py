"""
- Minimum Spanning Tree - MST (Cây khung nhỏ nhất) là tập hợp một số cạnh của đồ thị VÔ HƯỚNG có TRỌNG SỐ,
 sao cho tạo thành một cây CHỨA TẤT CẢ CÁC ĐỈNH với tổng trọng số các cạnh là nhỏ nhất.
- Prim's Algorithm là thuật toán tham lam dùng để tìm cây khung nhỏ nhất của đồ thị.
- ĐPT: O(E*logV)
"""
from queue import PriorityQueue


class Node:
    def __init__(self, p_id, distance):
        self.p_id = p_id
        self.dist = distance

    def __lt__(self, other):
        return self.dist <= other.dist


def print_mst():
    """
    Print the Minimum Spanning Tree
    """
    ans = 0
    for i in range(v):
        if path[i] == -1:
            continue
        ans += dist[i]
        print("{0} - {1}: {2}".format(path[i], i, dist[i]))
    print("Weight of MST: {0}".format(ans))


def prims(src):
    pq = PriorityQueue()
    pq.put(Node(src, 0))
    dist[src] = 0

    while not pq.empty():
        top = pq.get()
        u = top.p_id
        visited[u] = True

        for neighbor in graph[u]:
            v = neighbor.p_id
            w = neighbor.dist
            # if dist[u] != w:
            #     continue
            if not visited[v] and w < dist[v]:
                dist[v] = w
                pq.put(neighbor)
                path[v] = u


if __name__ == '__main__':
    INF = 10 ** 9

    v, e = map(int, input().split())
    graph = [[] for _ in range(v)]
    for _ in range(e):
        d = list(map(int, input().split()))
        graph[d[0]].append(Node(d[1], d[2]))
        graph[d[1]].append(Node(d[0], d[2]))

    dist = [INF for _ in range(v)]
    visited = [False for _ in range(v)]
    path = [-1 for _ in range(v)]

    prims(0)
    print_mst()
