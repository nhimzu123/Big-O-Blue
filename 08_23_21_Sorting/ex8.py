points = []
x_list = []
y_list = []

for i in range(8):
    line = input().split()
    x = int(line[0])
    y = int(line[1])
    x_list.append(x)
    y_list.append(y)
    points.append([x, y])

points.sort(key=lambda _: (_[0], _[1]))
x_list = list(set(x_list))
y_list = list(set(y_list))

if len(x_list) > 3 or len(y_list) > 3:
    print('ugly')
else:
    x_list.sort()
    y_list.sort()

    other_points = []
    for i in range(3):
        for j in range(3):
            other_points.append([x_list[i], y_list[j]])
    other_points.pop(4)
    check = True
    for i in range(8):
        if points[i][0] == other_points[i][0] and points[i][1] == other_points[i][1]:
            pass
        else:
            check = False
            break
    print("respectable" if check else "ugly")
