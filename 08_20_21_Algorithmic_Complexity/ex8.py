"""
Alice Bob and Chocolate
"""

n = int(input())
chocolates = [int(_) for _ in input().split()]

time_alice = 0
time_bob = 0
i = 0
j = n - 1

while i <= j:
    if time_alice + chocolates[i] <= time_bob + chocolates[j]:
        time_alice += chocolates[i]
        i += 1
    else:
        time_bob += chocolates[j]
        j -= 1

print(i, n - i)
