"""
Codechef: Restaurant Rating
"""

from heapq import heappush, heappop, heapreplace


N = int(input())
heap1, minheap = [], []
n = 0
for _ in range(N):
    z = input().split()
    if int(z[0]) == 2:
        if n < 3:
            print("No reviews yet")
        else:
            print(minheap[0])
    else:
        n += 1
        x = int(z[1])
        if n > 3 and minheap[0] < x and n % 3 != 0:
            x = heapreplace(minheap, x)
        heappush(heap1, -x)
        if n % 3 == 0:
            heappush(minheap, -heappop(heap1))
