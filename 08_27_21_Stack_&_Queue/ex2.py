"""
Street Parade
"""


def order(num, trucks):
    true_order = sorted(trucks)

    next_car = 1
    tmp_queue = []
    true_queue = []
    i = 0
    while i < num:
        if trucks[i] == next_car:
            true_queue.append(trucks[i])
            next_car += 1
            i += 1
        elif tmp_queue and tmp_queue[-1] == next_car:
            true_queue.append(tmp_queue[-1])
            tmp_queue.pop()
            next_car += 1
        else:
            tmp_queue.append(trucks[i])
            i += 1
    while tmp_queue and tmp_queue[-1] == next_car:
        next_car += 1
        true_queue.append(tmp_queue[-1])
        tmp_queue.pop()

    print('yes' if true_queue == true_order else "no")


if __name__ == '__main__':
    n_list = []
    trucks_list = []
    while True:
        n = int(input())
        if n == 0:
            break
        trucks = [int(_) for _ in input().split()]
        n_list.append(n)
        trucks_list.append(trucks)

    for k in range(len(n_list)):
        order(n_list[k], trucks_list[k])
    # order(6, [3, 2, 1, 4, 5, 6])

