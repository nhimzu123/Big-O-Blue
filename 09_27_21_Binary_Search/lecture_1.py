"""
- Binary Search là thuật toán tìm kiếm một phân tử trong mảng ĐÃ ĐƯỢC SẮP XẾP.
- Độ phức tạp: O(logN)
- BS dựa trên mối quan hệ giữa các giá trị để định hướng tìm kiếm -> chỉ áp dụng cho các mảng đã được sắp xếp
"""


def binary_search(a, left, right, x):
    """
    BS không sử dụng đệ quy
    :return: Position of x, if return -1 -> not found
    """
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_recursion(a, left, right, x):
    """
    BS sử dụng đệ quy
    """
    if left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        if a[mid] < x:
            return binary_search(a, mid + 1, right, x)
        else:
            return binary_search(a, left, mid - 1, x)
    return -1


def bs_first(a, left, right, x):
    """
    Tìm kiếm phần tử đầu tiên bằng x trong một mảng có nhiều phần tử bằng nhau
    """
    if left <= right:
        mid = (left + right) // 2
        if (mid == left or x > a[mid - 1]) and a[mid] == x:
            return mid
        elif a[mid] < x:
            return bs_first(a, mid + 1, right, x)
        else:
            return bs_first(a, left, mid - 1, x)
    return -1


def bs_last(a, left, right, x):
    """
    Tìm kiếm phần tử cuối cùng bằng x trong một mảng có nhiều phần tử bằng nhau.
    """
    if left <= right:
        mid = (left + right) // 2
        if (mid == right or x < a[mid + 1]) and a[mid] == x:
            return mid
        elif a[mid] < x:
            return bs_first(a, mid + 1, right, x)
        else:
            return bs_first(a, left, mid - 1, x)
    return -1


if __name__ == '__main__':
    n, k = map(int, input().split())
    array = list(map(int, input().split()))
    index = binary_search(array, 0, n - 1, k)
    # index = bs_last(array, 0, n - 1, k)
    # index = bs_first(array, 0, n - 1, k)
    # index = binary_search_recursion(array, 0, n - 1, k)

    print(f"Position of {k}: " + str(index) if index != -1 else "Not Found")
