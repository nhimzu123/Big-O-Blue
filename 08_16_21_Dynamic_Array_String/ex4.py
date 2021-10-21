"""
Vitaly and Strings
"""

# Algorithm: Tìm sâu S' = (S+1). Nếu S' < T thì tìm được chuỗi cần tìm, nếu S'= T thì "No such string"
# Steps:
# 1. Duyệt ngược chuỗi S
# 2.Nếu ký tự i là 'z' tiếp tục vòng lặp. Nếu ký tự i không phải 'z', thì thay ký tự đó bằng (i+1).

s = input()
t = input()

m = ""

for i in range(len(s) - 1, -1, -1):
    if s[i] == 'z':
        continue
    else:
        m = s[:i] + chr(ord(s[i]) + 1) + s[i + 1:]
        break
print(m if s < m < t else "No such string")
