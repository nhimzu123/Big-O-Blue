"""
Big Segment
"""
N = int(input())
i = 1
array = []
set1 = set()
while i <= N:
    a = [int(_) for _ in input().split()]
    array.append(a)
    set1.update(a)
    i += 1

min_start_pos = min(set1)
max_end_pos = max(set1)
good = False
pos = 1
for item in array:
    if item[0] == min_start_pos and item[1] == max_end_pos:
        good = True
        break
    else:
        pos += 1

print(pos if good else "-1")
