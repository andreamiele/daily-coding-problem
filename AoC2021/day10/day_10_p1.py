if __name__ == '__main__':
    import os
    with open(os.path.join(os.path.dirname(__file__), "input.txt"))as f:
        raw_data = f.read().strip()
data = raw_data.split("\n")

pairs = ["()", "[]", "<>", "{}"]
scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}


def parse(line):
    stack = []
    for char in line:
        good = False
        for p in pairs:
            if char == p[0]:
                stack.append(char)
                good = True
            elif char == p[1]:
                if stack[-1] == p[0]:
                    stack.pop()
                    good = True

        if not good:
            return scores[char]

    return 0


ans = 0
for line in data:
    ans += parse(line)

print(ans)
