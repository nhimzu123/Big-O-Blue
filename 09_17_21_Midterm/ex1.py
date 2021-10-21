"""
UVA: Printer Queue
"""

from queue import PriorityQueue


class Node:
    def __init__(self, index, value):
        self.index = index
        self.value = value

    def __lt__(self, other):
        return self.value > other.value


for _ in range(int(input())):
    pq = PriorityQueue()
    n, m = map(int, input().split())

    a = [int(num) for num in input().split()]
    for i in range(n):
        pq.put(Node(i, a[i]))
    time = 0
    while not pq.empty():
        top = pq.get()
        time += 1
        if top.index == m:
            break
    print(time)
