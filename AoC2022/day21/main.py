#Part 1

monkeys = {}

tab = [line.strip() for line in open(0)]

for obj in tab:
    name, expr = obj.split(": ")
    if expr.isdigit():
        monkeys[name] = int(expr)
    else:
        left, op, right = expr.split()
        if left in monkeys and right in monkeys:
            monkeys[name] = eval(f"{monkeys[left]} {op} {monkeys[right]}")
        else:
            tab.append(obj)

print(monkeys["root"])

#Part 2
#pip3 install sympy
import sympy

monkeys = { "humn": sympy.Symbol("x") }

tab = [line.strip() for line in open(0)]

ops = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}

for obj in tab:
    name, expr = obj.split(": ")
    if name in monkeys: continue
    if expr.isdigit():
        monkeys[name] = sympy.Integer(expr)
    else:
        left, op, right = expr.split()
        if left in monkeys and right in monkeys:
            if name == "root":
                print(sympy.solve(monkeys[left] - monkeys[right])[0])
                break
            monkeys[name] = ops[op](monkeys[left], monkeys[right])
        else:
            tab.append(obj)
