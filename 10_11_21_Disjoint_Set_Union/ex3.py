"""
UVA: Forests
"""


def find_set(u, index):
    if parents[index][u] != u:
        parents[index][u] = find_set(parents[index][u])


if __name__ == '__main__':
    MAX = 100
    for _ in range(int(input())):
        input()
        parents = [[_ for _ in range(MAX)] for _ in range(MAX)]
        ranks = [[0 for _ in range(MAX)] for _ in range(MAX)]
