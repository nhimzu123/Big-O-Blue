"""
Codeforces Problem 731A: Night at the Museum
"""

num_steps = 0
cur_id_char = 97

for c in input():

    if ord(c) == cur_id_char:
        pass
    elif ord(c) < cur_id_char:
        num_steps += min(cur_id_char - ord(c), (ord(c) - 97) + (123 - cur_id_char))
        cur_id_char = ord(c)
    else:
        num_steps += min(ord(c) - cur_id_char, (cur_id_char - 97) + (123 - ord(c)))
        cur_id_char = ord(c)

print(num_steps)