"""
Codeforces: Approximating a Constant Range
"""

n = int(input())

a = list(map(int, input().split()))

max_len = 0
j = 0
freq = [0] * (10**5 + 1)
unique = 0

for i in range(n):
    if freq[a[i]] == 0:
        unique += 1
    freq[a[i]] += 1

    while j < n and unique > 2:
        if freq[a[j]] == 1:
            unique -= 1
        freq[a[j]] -= 1
        j += 1

    max_len = max(max_len, i - j + 1)

print(max_len)
