"""
Chores
"""
line_1 = input().split()
n = int(line_1[0])
a = int(line_1[1])
b = int(line_1[2])
works = [int(_) for _ in input().split()]

works.sort()
vasya_works = works[:b]
petya_work = works[b:]
x = petya_work[0] - vasya_works[-1]
print(x)
