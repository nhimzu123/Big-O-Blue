"""
HackerRank: Breadth First Search
"""
from queue import Queue


def breadth_first_search(s, graph_li, path_li, visited_li):
    visited_li[s - 1] = True
    queue = Queue()
    queue.put(s)

    while not queue.empty():
        u = queue.get()
        for v in graph_li[u - 1]:
            if not visited_li[v - 1]:
                visited_li[v - 1] = True
                queue.put(v)
                path_li[v - 1] = u

    return path_li


def print_path(s, f, path_li):
    if s == f:
        print(f, end=' ')
    else:
        if path_li[f - 1] == -1:
            print("No path")
        else:
            print_path(s, f, path_li[f - 1])
            print(f, end=' ')


if __name__ == '__main__':
    q = int(input())
    n, m = map(int, input().split())

    graph = [[] for _ in range(n)]
    path = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]

    for _ in range(m):
        query = input()
        graph[int(query.split()[0]) - 1].append(int(query.split()[1]))

    s = int(input())

    res_path = breadth_first_search(s, graph, path, visited)
    print(res_path)
    # print_path(s=s, f=3, path_li=res_path)