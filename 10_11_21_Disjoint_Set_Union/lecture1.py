"""
- Disjoint Set Union (DSU): hay còn được gọi khác như Disjoint-Set, Union-Find là CTDL dùng để hợp
các phần tử lại với nhau thành những tập hợp lớn hơn.
- Cấu trúc DSU này cho phép thực hiện 3 thao tác cơ bản:
 * makeSet(): Tạo ra tập hợp cho mỗi phần từ ban đầu.
 * findSet(): Tìm đại diện của tập hợp chứa u.
 * unionSet(u,v): Hợp tập hợp chứa u và tập hợp chứa v thành một tập hợp lớn.
Nếu 2 phần tử u và v thuộc cùng một tập hợp thì thao tác này sẽ không thực hiện.
- ĐPT cho mỗi thao tác: O(N)
"""


def make_set(maximum):
    par = [_ for _ in range(maximum + 5)]
    return par


def find_set(u):
    while u != parent[u]:
        u = parent[u]
    return u


def union_set(u, v):
    up = find_set(u)
    vp = find_set(v)
    parent[up] = vp


if __name__ == '__main__':
    MAX = 20
    parent = make_set(MAX)

    queries = int(input())

    for i in range(queries):
        u, v, q = map(int, input().split())
        if q == 1:
            union_set(u, v)
        elif q == 2:
            u_parent = find_set(u)
            v_parent = find_set(v)
            print("YES" if u_parent == v_parent else "NO")
