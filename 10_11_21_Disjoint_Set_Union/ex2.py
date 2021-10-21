"""
UVA: Graph Connectivity
"""


def make_set(maximum):
    par = [_ for _ in range(maximum)]
    rank = [0 for _ in range(maximum)]
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
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    MAX = 26
    for _ in range(int(input())):
        input()
        parent, ranks = make_set(MAX)
        numbers = [0 for _ in range(MAX)]

        first_verticle = input()
        ranks[letters.index(first_verticle)] = 1

        while True:
            query = input()
            if query == "":
                break
            union_set(letters.index(query[0]), letters.index(query[1]))

        for k in range(MAX):
            my_parent = find_set(k)
            numbers[my_parent] += 1
        count = 0
        for nu in numbers:
            if nu != 1 or nu != 0:
                count += 1
        print(count)
