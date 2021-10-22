"""
HackerRank: Breadth-First-Search: Shortest Path
"""

from queue import Queue


def bfs(s):
    q = Queue()
    visited[s] = True
    q.put(s)

    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.put(v)
                path[v] = u
                dist[v] = dist[u] + 1


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())

        path = [-1 for _ in range(n+1)]
        visited = [False for _ in range(n+1)]
        graph = [[] for _ in range(n+1)]
        dist = [0] * (n+1)

        for _ in range(m):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)
        
        s = int(input())
        
        bfs(s)

        for nu in range(1, n+1):
            if nu != s:
                print(dist[nu] * 6 if dist[nu] != 0 else -1, end=" ")
        print()