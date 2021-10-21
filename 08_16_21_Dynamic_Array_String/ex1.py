so_khuy = int(input())
khuy_ao = input().split()

if len(khuy_ao) > 1:
    print('YES' if khuy_ao.count('0') == 1 else 'NO')
else:
    print('NO' if khuy_ao[0] == '0' else 'YES')
