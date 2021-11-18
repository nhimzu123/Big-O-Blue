"""
- Heap (Đống) là cấu trúc cây nhị phân hoàn chỉnh (complete binary tree)
- Có 2 loại Heap:
    * Min-heap: Mỗi node cha đều có giá trị nhỏ hơn hoặc bằng node con.
    * Max-heap: Mỗi node cha đều có giá trị lớn hơn hoặc bằng node con.

- Độ phức tạp của các thao tác trên Heap:
    * Xây dựng cây Heap từ mảng: O(n)
    * Tìm phần tử lớn nhất/nhỏ nhất trên Heap: O(1)
    * Thêm 1 phần tử vào Heap: O(log(n))
    * Xóa 1 phần tử vào Heap: O(log(n))
"""


def min_heapify(i):
    """
    Normalize the min-Heap
    """
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < len(h) and h[left] < h[smallest]:
        smallest = left
    if right < len(h) and h[right] < h[smallest]:
        smallest = right

    if smallest != i:
        h[i], h[smallest] = h[smallest], h[i]
        min_heapify(smallest)


def max_heapify(i):
    """
    Normalize the max-Heap
    """
    biggest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < len(h) and h[left] > h[biggest]:
        biggest = left
    if right < len(h) and h[right] > h[biggest]:
        biggest = right

    if biggest != i:
        h[i], h[biggest] = h[biggest], h[i]
        max_heapify(biggest)


def push(value):
    """
    Add a value to min/max-Heap and normalize that Heap.
    :param value: int
    """
    h.append(value)
    i = len(h) - 1

    # while i != 0 and h[(i - 1) // 2] > h[i]:  # used for min Heap
    while i != 0 and h[(i - 1) // 2] < h[i]:  # used for max Heap
        h[i], h[(i - 1) // 2] = h[(i - 1) // 2], h[i]
        i = (i - 1) // 2


def top():
    """
    Return the smallest/biggest value of min/max-Heap.
    """
    return h[0]


def pop():
    """
    Delete the value at index-th node.
    :param index: int
    """
    length = len(h)
    h[0] = h[length - 1]
    h.pop()
    # min_heapify(0)  # for min-Heap
    max_heapify(0)  # for max-Heap


def build_heap(n):
    for i in range(n // 2 - 1, -1, -1):
        # Build a min-Heap
        # min_heapify(i)
        # Build a max-Heap
        max_heapify(i)


if __name__ == '__main__':
    h = [7, 12, 6, 10, 17, 15, 2, 4]

    # Build Heap
    build_heap(len(h))
    print(h)
    # Add a value to the Heap
    push(3)
    print(h)
    # Print the smallest/biggest value of the Heap
    print("The smallest/biggest value of the Heap:", top())
    # Delete the 0-th node
    pop()
    print(h)
