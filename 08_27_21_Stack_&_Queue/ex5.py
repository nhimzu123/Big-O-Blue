"""
Spoj: Mass of Molecule
"""

stack = []
mass = {
    'C': 12,
    'H': 1,
    'O': 16
}

for char in input().strip():
    if char.isalpha():
        stack.append(mass[char])
    elif char.isnumeric():
        mol = stack[-1] * int(char)
        stack.pop()
        stack.append(mol)
    elif char == "(":
        stack.append(-1)
    elif char == ")":
        w = 0
        while stack[-1] != -1:
            w += stack[-1]
            stack.pop()
        stack.pop()
        stack.append(w)

print(sum(stack))
