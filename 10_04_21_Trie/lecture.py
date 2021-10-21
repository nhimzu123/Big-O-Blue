"""
- Trie (Cây tiền tố) là một cấu trúc dữ liệu dạng cây dùng để lưu danh sách các từ trên cây. Trie là một cây nhưng
KHÔNG PHẢI CÂY NHỊ PHÂN, nó là cấu trúc cây bình thường nhưng với việc lưu các từ theo dạng cấu trúc tiền tố giúp
cho việc Thêm (add/insert), Xoá (delete/remove) và Tìm Kiếm (search/find) trở nên hiệu quả hơn.
- Một cây Trie gồm nhiều node, mỗi node gồm 2 thành phần:
    * Một node chứa dữ liệu. Node này có thể liên kết với node khác.
    * Một biến số nguyên. Nếu số nguyên khác 0 nghĩa là node đó là kết thúc của một từ.
"""


class Node:
    def __init__(self):
        self.countWord = 0
        self.child = dict()


# Thao tác trên cây Trie - ĐPT: O(string_length)
def add_word(root, string):
    """
    Add a string to Trie
    :param root: Cây Trie
    :param string: từ cần thêm
    """
    temp = root
    for ch in string:
        if ch not in temp.child:
            temp.child[ch] = Node()

        temp = temp.child[ch]


def find_word(root, string):
    """
    Tìm một chuỗi trong cây Trie
    :param root: cây Trie
    :param string: chuỗi cần tìm
    """
    temp = root
    for ch in string:
        if ch not in temp.child:
            return False
        temp = temp.child[ch]

    return temp.countWord > 0


def is_word(node):
    return node.countWord != 0


def is_empty(node):
    return len(node.child) == 0


def remove_word(root, string, level, length):
    """
    Xoá một sâu khỏi cây Trie
    """
    if root is None:
        return False
    if level == length:
        if root.countWord > 0:
            root.countWord = -1
            return True
        return False

    ch = string[level]
    if ch not in root.child:
        return False

    flag = remove_word(root.child[ch], string, level + 1, length)
    if flag and not is_word(root.child[ch]) and is_empty(root.child[ch]):
        del root.child[ch]
    return flag


def print_word(root, string):
    if is_word(root):
        print(string)
    for ch in root.child:
        print_word(root.child[ch], string + ch)


if __name__ == '__main__':
    root = Node()
    add_word(root, "the")
    add_word(root, "then")
    add_word(root, "bigo")

    print_word(root, "")

    # print(root.child)
    # print(root.countWord)
    # print(find_word(root, "there"))
    # print(find_word(root, "th"))
    # print(find_word(root, "the"))

    # remove_word(root, "bigo", 0, 4)
    # remove_word(root, "the", 0, 3)
    # remove_word(root, "then", 0, 4)
