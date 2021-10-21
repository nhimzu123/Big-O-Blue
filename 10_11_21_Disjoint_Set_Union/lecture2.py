"""
- Union By Rank & Path Compression: là phương pháp Union các node lại theo rank của node và nén
đường đi để việc truy vết đỉnh cha được nhanh hơn.
- ĐPT cho mỗi thao tác: O(logN)
"""


def make_set(maximum):
    par = [_ for _ in range(maximum + 5)]
    rank = [0 for _ in range(maximum + 5)]
    return par, rank


def find_set(u):
    if parent[u] != u:
        parent[u] = find_set(parent[u])
    return parent[u]


def union_set(u, v):
    u_parent = find_set(u)
    v_parent = find_set(v)
    if u_parent == v_parent:
        return
    if ranks[u_parent] > ranks[v_parent]:
        parent[v_parent] = u_parent
    elif ranks[u_parent] < ranks[v_parent]:
        parent[u_parent] = v_parent
    else:
        parent[u_parent] = v_parent
        ranks[v_parent] += 1


if __name__ == '__main__':
    MAX = 20
    parent, ranks = make_set(MAX)

    for i in range(int(input())):
        a, b, q = map(int, input().split())
        if q == 1:
            union_set(a, b)
        elif q == 2:
            a_parent = find_set(a)
            b_parent = find_set(b)
            print("YES" if a_parent == b_parent else "NO")
