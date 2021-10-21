"""
- Breadth-First Search (BFS) Algorithm: Thuật toán tìm kiếm trên đồ thị vô hướng hoặc có hướng,
KHÔNG TRỌNG SỐ, nếu có trọng số thì tất cả phải bằng nhau.
- BFS luôn tìm được đường đi ngắn nhất (nếu tồn tại đường đi).
- ĐPT: O(V+E)
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

def print_path(s, f):
    b = []
    if f == s:
        print(s)
        return
    if path[f] == -1:
        print("No path!")
        return
    while True:
        b.append(f)
        f = path[f]
        if f == s:
            b.append(s)
            break

    for i in range(len(b)-1,-1,-1):
        print(b[i], end=" ")


def print_path_recursion(s, f):
    if s == f:
        print(f, end=" ")
    else:
        if path[f] == -1:
            print("No path")
        else:
            print_path_recursion(s, path[f])
            print(f, end=" ")


if __name__ == '__main__':
    MAX = 100
    visited = [False for _ in range(MAX)]
    path = [-1 for _ in range(MAX)]
    graph = [[] for _ in range(MAX)]

    v, e = map(int, input().split())
    for _ in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    s = 0
    f = 5
    bfs(s)
    print_path(s, f)


