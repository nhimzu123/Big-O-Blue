def additional_problems(n, m, good_complexity, problems):
    index = 0
    count = 0

    while count < n and index < m:
        if problems[index] >= good_complexity[count]:
            count += 1
        index += 1

    return n - count


if __name__ == '__main__':
    line_1 = input().split()
    n = int(line_1[0])
    m = int(line_1[1])
    good_complexities = [int(_) for _ in input().split()]
    problems = [int(_) for _ in input().split()]

    print(additional_problems(n, m, good_complexities, problems))
