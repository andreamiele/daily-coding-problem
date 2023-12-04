import re

r = 0

with open('input.txt', 'r') as f:
    lines = [x.strip() for x in f.readlines()]
    for line in lines:
        left, right = line.split("|")
        left_nums = re.findall(r"\d+", left)[1::]
        right_nums = re.findall(r"\d+", right)

        common = set(left_nums).intersection(right_nums)

        if len(common) > 0:
            r += 2 ** (len(common) - 1)

print(r)


s = {}

with open('input.txt', 'r') as f:
    lines = [x.strip() for x in f.readlines()]
    for i, line in enumerate(lines):
        if i not in s:
            s[i] = 1

        left, right = line.split("|")
        left_nums = re.findall(r"\d+", left)[1::]
        right_nums = re.findall(r"\d+", right)

        common = set(left_nums).intersection(right_nums)

        if len(common) == 0:
            continue

        for n in range(i + 1, i + len(common) + 1):
            s[n] = s.get(n, 1) + s[i]

print(sum(s.values()))