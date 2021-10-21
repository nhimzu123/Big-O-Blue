"""
Towers
"""

n = int(input())

woods = [int(_) for _ in input().split()]

woods.sort()

freq = [0] * 1001

for i in range(n):
    freq[woods[i]] += 1

num_of_towers = 0
for num in freq:
    if num != 0:
        num_of_towers += 1

print(max(freq), num_of_towers)
