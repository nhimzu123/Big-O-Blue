"""
Business Trip
"""

k = int(input())
months = [int(_) for _ in input().split()]

months.sort(reverse=True)
water = 0
count = 0
if k == 0:
    print(0)
else:
    for i in range(12):
        water += months[i]
        count += 1
        if water >= k:
            break
    if water < k:
        print(-1)
    else:
        print(count)
