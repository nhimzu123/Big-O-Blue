"""
Codeforces: Wrath
"""

n = int(input())
a = [int(_) for _ in input().split()]

count = 0
j = n - 1

for i in range(n - 1, -1, -1):
    j = min(j, i)
    last_kill_pos = max(0, i - a[i])

    if j > last_kill_pos:
        count += (j - last_kill_pos)
        j = last_kill_pos

print(n - count)
