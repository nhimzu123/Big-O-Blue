"""
SPOJ: Promotion
"""

from heapq import heappop, heappush

cost = 0
lookup = []
# max_heap = []
min_heap = []
for i in range(int(input())):
    command = list(map(int, input().split()))

    for _ in range(command[0]):
        heappush(min_heap, command[_ + 1])
        lookup.append(command[_ + 1])
    max_bill = max(lookup)
    min_bill = min_heap[0]
    