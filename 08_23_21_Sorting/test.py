n = 5
a = [3, 5, 4, 5, 3]
freq = [0] * (max(a) + 1)
print(freq)
for i in range(n):
    freq[a[i]] += 1

print(freq)
