"""
Sort the array
"""

n = int(input())
array = [int(_) for _ in input().split()]

sorted_array = sorted(array)

i = 0
j = n - 1

for i in range(n):
    if array[i] == sorted_array[i]:
        i += 1
    else:
        break

for j in range(j, -1, -1):
    if array[j] == sorted_array[j]:
        j -= 1
    else:
        break

array[i:j + 1] = array[i:j + 1][::-1]

if array == sorted_array:
    print("yes")
    if j <= 0 and i >= n:
        print(1, 1)
    else:
        print(i + 1, j + 1)
else:
    print("no")
