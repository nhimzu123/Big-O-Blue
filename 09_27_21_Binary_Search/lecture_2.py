"""
Sử dụng Python Library để sử dụng Binary Search
"""
import bisect

if __name__ == '__main__':
    a = [1, 1, 2, 2, 2, 3, 4, 5, 6]
    n, x = 9, 3

    # `bisect_left` trả về vị trí đầu tiên LỚN HƠN HOẶC BẰNG giá trị đang tìm kiếm trong đoạn [first, last)
    first_pos = bisect.bisect_left(a, x, 0, n)
    print(first_pos)

    # `bisect_right` trả về vị trí đầu tiên LỚN HƠN giá trị tìm kiếm trong đoạn [first, last)
    pos = bisect.bisect_right(a, x, 0, n)
    print(pos)

