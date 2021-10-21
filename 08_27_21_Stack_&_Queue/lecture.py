from queue import Queue

q = Queue()

# Them
q.put(5)
q.put(3)
q.put(2)

# -> Queue = |2, 3, 5| - 5 là phần tử đầu tiên đưa vào hàng đợi, 2 là phần tử sau cùng đưa vào hàng đợi

# Lấy phần tử cuối cùng (phần tử đầu tiên đc đưa vào queue) ra và xoá nó
s = q.get()

# Lấy phần tử cuối cùng ra

value = q.queue[0]
print(value)

# Size của queue
size = q.qsize()

# Kiểm tra queue rỗng:
is_empty = q.empty()

