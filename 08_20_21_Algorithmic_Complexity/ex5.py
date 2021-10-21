"""
Codeforces: Sereja and Dima
"""

n = int(input())
cards = list(map(int, input().split()))

sereja_mark = 0
dima_mark = 0

for i in range(n):
    if i % 2 == 0:
        if cards[-1] > cards[0]:
            sereja_mark += cards[-1]
            cards.pop()
        else:
            sereja_mark += cards[0]
            cards.pop(0)
    else:
        if cards[-1] > cards[0]:
            dima_mark += cards[-1]
            cards.pop()
        else:
            dima_mark += cards[0]
            cards.pop(0)

print(sereja_mark, dima_mark)
