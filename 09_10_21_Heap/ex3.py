"""
UVa: Add All
"""

import heapq

while True:
    n = int(input())
    if n == 0:
        break
    a = list(map(int, input().split()))
    min_heap = []
    for num in a:
        heapq.heappush(min_heap, num)

    cost = 0
    total_cost = 0
    while len(min_heap) > 1:
        total_cost = min_heap[0]
        heapq.heappop(min_heap)
        total_cost += min_heap[0]
        heapq.heappop(min_heap)
        cost += total_cost
        heapq.heappush(min_heap, total_cost)

    print(cost)

