"""
Pasha and Tea
"""
line_1 = input().split()
n = int(line_1[0])
w = int(line_1[1])

cups_of_tea = [int(_) for _ in input().split()]

cups_of_tea.sort()
low_capa_cup = cups_of_tea[0]
high_capa_cup = cups_of_tea[n]

tea = 0
if low_capa_cup * 2 > high_capa_cup:
    tea = high_capa_cup * n * 1.5
else:
    tea = low_capa_cup * n * 3

print(min(w, tea))
