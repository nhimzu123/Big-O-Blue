a = [1, 3, 6, 8, 10]
b = [2, 6, 7, 12, 14, 15]
n = len(a)  # 5
m = len(b)  # 6

i = 0
j = 0
c = []
while i < n or j < m:
    try:
        if (a[i] <= b[j] and i < n) or j == m:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    except IndexError:
        print(i, j)
        break
print(c)


