"""
Uva: That is your queue
"""
from collections import deque


def your_queue(p, c, command_list):
    result = []

    q = deque()
    for _ in range(1, min(p, c) + 1):
        q.append(_)

    # pdb.set_trace()
    for cmd in command_list:
        if cmd == 'N':
            # print(q[0])
            result.append(q[0])
            q.append(q.popleft())
        else:
            x = int(cmd.split()[1])
            n = len(q)
            q.append(x)
            for i in range(n):
                temp = q.popleft()
                if temp != x:
                    q.append(temp)
    return result


if __name__ == '__main__':

    results = []
    while True:
        P, C = map(int, input().split())
        if P == 0 and C == 0:
            break

        commands = []
        for _ in range(C):
            line = input()
            commands.append(line)

        results.append(your_queue(P, C, commands))

    tc = 1
    for res in results:
        print('Case {}:'.format(tc))
        tc += 1
        for out in res:
            print(out)
