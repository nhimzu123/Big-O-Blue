"""
Throwing Cards Away 1
"""


def throw_card(num):
    origin_order = [_ for _ in range(1, num + 1)]
    discarded_cards = []
    remain_card = 0

    for i in range(num):
        if len(origin_order) == 1:
            remain_card = origin_order[0]
            break
        discarded_cards.append(str(origin_order[0]))
        origin_order.pop(0)
        origin_order.append(origin_order[0])
        origin_order.pop(0)

    if discarded_cards:
        print("Discarded cards:", ', '.join(discarded_cards))
    else:
        print("Discarded cards:")
    print("Remaining card:", remain_card)


if __name__ == '__main__':
    n_list = []
    while True:
        n = int(input())
        if n == 0:
            break
        else:
            n_list.append(n)

    for n in n_list:
        throw_card(n)
