"""
Codechef: Compilers and Parsers
"""    

def check(s):
    cost = 0
    stack = []

    for i in range(len(s)):
        if s[i] == "<":
            stack.append(s[i])
        elif not stack:
            break
        else:
            stack.pop()
            cost = i + 1 if not stack else cost

    return cost

for i in range(int(input())):
    string = input()
    print(check(string))
