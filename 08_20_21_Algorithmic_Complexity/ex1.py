"""
Books
"""


def count_book(n, t, minutes):
    count_of_books = 0
    k = 0
    sum_of_time = 0
    for i in range(n):
        sum_of_time += minutes[i]
        if sum_of_time <= t:
            count_of_books += 1
        else:
            sum_of_time -= minutes[k]
            k += 1

    return count_of_books


def books(n, t, minutes):
    max_book = 0
    start_book = 0
    read_time = 0

    for end_book in range(n):
        read_time += minutes[end_book]

        while read_time > t:
            read_time -= minutes[start_book]
            start_book += 1

        max_book = max(max_book, end_book - start_book + 1)

    return max_book


if __name__ == '__main__':
    n, t = map(int, input().split())
    minutes = [int(_) for _ in input().split()]

    # print(count_book(n, t, minutes))
    print(books(n, t, minutes))
