if __name__ == '__main__':
    import os
    with open(os.path.join(os.path.dirname(__file__), "input.txt"))as f:
        raw_data = f.read().strip().split(",")
        clocks = [int(i) for i in raw_data]


# After 80 days, something like 11 cycles will have gone by
# That's a growth rate of more than 2000!
# We can probably still brute force this
days = 80

for _ in range(days):
    n = len(clocks)
    for i in range(n):
        if clocks[i] == 0:
            clocks[i] = 6
            clocks.append(8)
        else:
            clocks[i] -= 1

ans = len(clocks)
print(ans)
