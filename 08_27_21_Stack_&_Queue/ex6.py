"""
Ferry Loading III
"""
from queue import Queue


class Car:
    def __init__(self, time, position):
        self.time = time
        self.pos = position


if __name__ == '__main__':
    for _ in range(int(input())):
        n, t, m = map(int, input().split())
        left_queue = Queue()
        right_queue = Queue()
        for i in range(m):
            ti, pos = input().split()
            if pos == 'left':
                left_queue.put(Car(int(ti), pos))
            else:
                right_queue.put(Car(int(ti), pos))
        cur_pos = 'left'
        cur_time = 0
        ans = [0 for _ in range(m)]

        while not left_queue.empty() and not right_queue.empty():
            pass
