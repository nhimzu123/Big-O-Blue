"""
UVA: Friends
"""


def make_set(maximum):
    par = [_ for _ in range(maximum + 1)]
    rank = [0 for _ in range(maximum + 1)]
    return par, rank


def find_set(u):
    if parent[u] != u:
        parent[u] = find_set(parent[u])
    return parent[u]


def union_set(u, v):
    u_p = find_set(u)
    v_p = find_set(v)
    if u_p == v_p:
        return
    if ranks[u_p] > ranks[v_p]:
        parent[v_p] = u_p
    elif ranks[u_p] < ranks[v_p]:
        parent[u_p] = v_p
    else:
        parent[u_p] = v_p
        ranks[v_p] += 1


if __name__ == '__main__':
    for i in range(int(input())):
        n, m = map(int, input().split())
        parent, ranks = make_set(n)

        for j in range(m):
            a, b = map(int, input().split())
            union_set(a, b)

        numbers = [0 for _ in range(n + 1)]
        for k in range(1, n + 1):
            my_parent = find_set(k)
            numbers[my_parent] += 1

        print(max(numbers))
