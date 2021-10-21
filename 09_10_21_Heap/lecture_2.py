"""
Build a min/max Heap with Python libraries
"""

from queue import PriorityQueue  # Cách 1: Sử dụng Priority Queue
import heapq  # Cách 2: Sử dụng heapq. heapq sử dụng 1 biến list để xử lý.


class PQEntry:
    """
    To build a max-Heap, a new class should be built because the default Heap of Priority Queue and heapq is min-Heap.
    """
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value > other.value


a = [7, 12, 6, 10, 17, 15, 2, 4]

# -------------------- Cách 1: Build a min/max-Heap with Priority Queue --------------------
min_pq = PriorityQueue()
max_pq = PriorityQueue()

for num in a:
    # Build a max-Heap queue
    max_pq.put(PQEntry(num))
    # Build a min-Heap queue
    min_pq.put(num)

# ---------------------------------
# --- Methods of Priority Queue ---
# ---------------------------------

# Print the first node's value of queue
print(max_pq.queue[0])

# Add a new value to the Heap
min_pq.put(3)
max_pq.put(PQEntry(3))

# Remove the first node, then returns its value
first_value = max_pq.get().value

# Length of the Prioirty Queue
print(len(min_pq.queue))

# Check the empty PQ
print("It's empty" if min_pq.empty() else "It's not empty")


# -------------------- Cách 2: Build a min/max-Heap with heaqp --------------------

max_heapq = []
h = [7, 12, 6, 10, 17, 15, 2, 4]
for num in a:
    # Build a max-Heap
    heapq.heappush(max_heapq, PQEntry(num))

# Build a min-Heap
heapq.heapify(h)

# Print the first node's value of heap
print("Max value of max-Heap:", max_heapq[0].value)
print("Min value of min-Heap:", h[0])

# Add a node to the Heap
heapq.heappush(max_heapq, PQEntry(3))
heapq.heappush(h, 3)

# Remove the first node and return its value
first_value = heapq.heappop(max_heapq)
print(first_value.value)

# Clear the Heap
max_heapq.clear()
h.clear()
