"""
UVA: Where is the marble
"""


def bs_first(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2
        if (mid == left or x > a[mid - 1]) and a[mid] == x:
            return mid
        elif a[mid] < x:
            return bs_first(a, mid + 1, right, x)
        else:
            return bs_first(a, left, mid - 1, x)
    return -1


if __name__ == '__main__':
    case = 1
    while True:
        n, k = map(int, input().split())
        if n == 0 and k == 0:
            break

        array = []
        for i in range(n):
            array.append(int(input()))
        array.sort()
        print(f"CASE# {case}:")
        case += 1

        for i in range(k):
            num = int(input())
            pos = bs_first(array, 0, n - 1, num)
            if pos == -1:
                print(f"{num} not found")
            else:
                print(f"{num} found at {pos + 1}")
