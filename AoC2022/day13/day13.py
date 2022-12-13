if __name__ == '__main__':
    import os

    with open(os.path.join(os.path.dirname(__file__), "input.tlistet")) as f:
        data = f.read()

liste = list(map(str.splitlines, data.strip().split("\n\n")))

def f(liste, y):
    if type(liste) == int:
        if type(y) == int:
            return liste - y
        else:
            return f([liste], y)
    else:
        if type(y) == int:
            return f(liste, [y])
    
    for a, b in zip(liste, y):
        v = f(a, b)
        if v:
            return v
    
    return len(liste) - len(y)

t = 0

for i, (a, b) in enumerate(liste):
    if f(eval(a), eval(b)) < 0:
        t += i + 1

print(t)


def f(liste, y):
    if type(liste) == int:
        if type(y) == int:
            return liste - y
        else:
            return f([liste], y)
    else:
        if type(y) == int:
            return f(liste, [y])
    
    for a, b in zip(liste, y):
        v = f(a, b)
        if v:
            return v
    
    return len(liste) - len(y)

liste = list(map(eval, data.split()))

i = 1
j = 2

for a in liste:
    if f(a, [[2]]) < 0:
        i += 1
        j += 1
    elif f(a, [[6]]) < 0:
        j += 1

print(i * j)