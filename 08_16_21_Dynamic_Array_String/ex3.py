"""
Bear and Game
"""

N = int(input())
minutes = [int(_) for _ in input().split()]

start_time = 0
total_watching_time = 0

for minute in minutes:
    if start_time + 15 < minute:
        total_watching_time = start_time + 15
        break
    else:
        start_time = minute
        total_watching_time = start_time + 15


if total_watching_time > 90:
    total_watching_time = 90
print(total_watching_time)
