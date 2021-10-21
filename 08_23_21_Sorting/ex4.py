"""
Gukiz and Contest
"""

n = int(input())
ratings = [int(_) for _ in input().split()]
results = []

freq = [0] * (max(ratings) + 1)

for i in range(n):
    freq[ratings[i]] += 1

for rate in ratings:
    results.append(str(1 + sum(freq[rate + 1:])))

print(" ".join(results))
