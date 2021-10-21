def your_queue(p, c, queries):
    count = 0
    origin_pos = 1
    true_queue = []
    tmp_queue = []
    j = 1
    for i in range(c):
        if queries[i] == "N":
            if tmp_queue:
                true_queue.append(tmp_queue[-1])
                tmp_queue.pop()
            else:
                true_queue.append(j)
                j += 1
        else:
            tmp_queue.append(int(queries[i].split()[1]))

    print(true_queue)


your_queue(3, 6, ["N", "N", "E 1", "N", "N", "N"])
