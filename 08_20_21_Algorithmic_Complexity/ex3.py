"""
Codeforces: Dress'em in Vests!
"""


def dress_them_in(n_num, m_num, x_num, y_num, a_array, b_array):
    couples_li = []
    j = 0
    i = 0
    while i < n and j < m:
        if a_array[i] - x_num <= b_array[j] <= a_array[i] + y_num:
            couples_li.append((i + 1, j + 1))
            i += 1
            j += 1
        elif a_array[i] + y_num < b_array[j]:
            i += 1
        elif a_array[i] - x_num > b_array[j]:
            j += 1

    print(len(couples_li))
    for coup in couples_li:
        print(coup[0], coup[1])


if __name__ == '__main__':
    n, m, x, y = map(int, input().split())

    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    dress_them_in(n, m, x, y, a_list, b_list)
