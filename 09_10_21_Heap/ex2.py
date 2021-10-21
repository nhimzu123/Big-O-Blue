"""
Hackerrank: Qheap 1
"""

import heapq

min_heap = []
lookup = set()

for i in range(int(input())):
    command = list(map(int, input().split()))

    if command[0] == 1:
        heapq.heappush(min_heap, command[1])
        lookup.add(command[1])
    elif command[0] == 2:
        lookup.discard(command[1])
    else:
        while min_heap[0] not in lookup:
            heapq.heappop(min_heap)

        print(min_heap[0])
