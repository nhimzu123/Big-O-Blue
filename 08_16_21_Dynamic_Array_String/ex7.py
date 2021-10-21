"""
Passwords
"""
a = [int(_) for _ in input().split()]

n, k = a[0], a[1]
passwords = []
for i in range(n):
    passwords.append(input())
passwords.sort(key=len)

true_password = input()

len_array = {len(_) for _ in passwords}
standard_array = []

for length in len_array:
    standard_array.append([_ for _ in passwords if len(_) == length])

best_time = 0
worst_time = 0
pass_counter = 0

for codes in standard_array:
    pass_counter += len(codes)
    if true_password in codes:
        m = (pass_counter - len(codes)) % k
        l = (pass_counter - len(codes)) // k
        best_time = l * (k + 5) + m + 1
        o = (pass_counter - 1) % k
        p = (pass_counter - 1) // k
        worst_time = p * (k + 5) + o + 1

print(best_time, worst_time)