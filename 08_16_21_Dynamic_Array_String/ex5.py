"""
Arrays
"""
num_a, num_b = input().split()
k, m = input().split()

a_array = [int(_) for _ in input().split()]
b_array = [int(_) for _ in input().split()]

k_array = a_array[:int(k)]
m_array = b_array[-int(m):]
print(k_array)
print(m_array)

if max(k_array) < min(m_array):
    print('YES')
else:
    print('NO')