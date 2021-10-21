def calculate_minutes(n, x, subjects):
    sum_minutes = 0
    time_cost = x
    subjects.sort()
    for i in range(n):
        if time_cost > 1:
            sum_minutes += subjects[i] * time_cost
            time_cost -= 1
        else:
            sum_minutes += subjects[i] * 1

    return sum_minutes


if __name__ == '__main__':
    line_1 = input().split()
    n = int(line_1[0])
    x = int(line_1[1])

    subjects = [int(_) for _ in input().split()]
    print(calculate_minutes(n, x, subjects))
