"""
Codeforces Problem 448B: Suffix Structures
"""


def automaton(string_a, string_b):
    index = 0
    tmp_str = ""
    for i in range(len(string_a)):
        if index == len(string_b):
            break
        if string_a[i] == string_b[index]:
            tmp_str += string_a[i]
            index += 1
    return tmp_str == string_b


def array(string_a, string_b):
    return True if sorted(string_a) == sorted(string_b) else False


def need_tree(string_a, string_b):
    dict_a = {key: string_a.count(key) for key in string_a}
    dict_b = {key: string_b.count(key) for key in string_b}

    for key in dict_b.keys():
        if key not in dict_a.keys():
            return True
        if dict_b[key] > dict_a[key]:
            return True
    return False


if __name__ == '__main__':
    s = input()
    t = input()

    if automaton(s, t):
        print("automaton")
    elif array(s, t):
        print("array")
    elif need_tree(s, t):
        print("need tree")
    else:
        print("both")
