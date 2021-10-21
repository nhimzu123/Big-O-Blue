"""
Codeforces: MUH and Important things
"""

import queue
import math


class Scanner:
    def __generator__():
        while True:
            try:
                buff = input().strip().split()
                for x in buff:
                    yield x
            except EOFError:
                exit()

    sc = __generator__()

    def next():
        return Scanner.sc.__next__()


class Node:
    dist = 0
    index = 0

    def __init__(self, dist=0, index=0):
        self.dist = dist
        self.index = index

    def __lt__(self, other):
        return self.dist < other.dist


def prim(graph, src):
    # graph = matrix [n][n]
    n = len(graph)
    dist = [1e9] * n
    visited = [0] * n
    total_cost = 0
    dist[src] = 0
    pq = queue.PriorityQueue()
    pq.put(Node(0, src))

    while not pq.empty():
        temp = pq.get()
        u = temp.index
        visited[u] = True
        for v in range(n):
            if not visited[v] and dist[v] > graph[u][v]:
                dist[v] = graph[u][v]
                pq.put(Node(dist[v], v))

    for i in range(n):
        total_cost += dist[i]
    return total_cost


def distance(x1, y1, x2, y2):
    square_dis = (x1 - x2) ** 2 + (y1 - y2) ** 2
    return math.sqrt(square_dis)


def solve():
    for _ in range(int(input())):
        input()
        n = int(Scanner.next())
        x = [0] * n
        y = [0] * n
        for i in range(n):
            x[i], y[i] = float(Scanner.next()), float(Scanner.next())
        graph = []
        for i in range(n):
            graph.append([])
            for j in range(n):
                graph[i].append(distance(x[i], y[i], x[j], y[j]))

        print("%.2f\n" % prim(graph, 0))


solve()