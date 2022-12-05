if __name__ == '__main__':
    import os
    with open(os.path.join(os.path.dirname(__file__), "input.txt"))as f:
        data = f.read().strip().split("\n")


def parse_line(line):
    cmd, amount = line.split(" ")
    amount = int(amount)
    if cmd == "forward":
        return (amount, 0)
    elif cmd == "down":
        return (0, amount)
    else:
        return (0, -amount)


pos, depth = 0, 0

for line in data:
    dpos, ddepth = parse_line(line)
    pos += dpos
    depth += ddepth

ans = pos * depth
print(ans)
