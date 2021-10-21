"""
Transform the Expression
"""


def convert_rpn(expression):
    stack = []
    rpn = ""
    operand = ["+", "-", "*", "/", "^"]
    letter = [char for char in "qwertyuioplkjhgfdsazxcvbnm"]
    for i in range(len(expression)):
        if expression[i] in letter:
            rpn += expression[i]
        if expression[i] in operand:
            stack.append(expression[i])
        if expression[i] == ")":
            rpn += stack[-1]
            stack.pop()
    return rpn


if __name__ == '__main__':
    t = int(input())
    list_exp = []
    for i in range(t):
        list_exp.append(input())

    for exp in list_exp:
        print(convert_rpn(exp))
