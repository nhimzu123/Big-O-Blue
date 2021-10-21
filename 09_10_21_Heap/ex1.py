"""
Hackerearth
"""

from queue import PriorityQueue


class PQEntry:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value > other.value


max_pq = PriorityQueue()
n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    max_pq.put(PQEntry(a[i]))
    if len(max_pq.queue) < 3:
        print(-1)
    else:
        first = max_pq.get()
        second = max_pq.get()
        third = max_pq.get()

        max_pq.put(first)
        max_pq.put(second)
        max_pq.put(third)
        print(first.value * second.value * third.value)
