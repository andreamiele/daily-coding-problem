if __name__ == '__main__':
    import os
    with open(os.path.join(os.path.dirname(__file__), "input.txt"))as f:
        raw_data = f.read().strip().split(",")

data = [int(i) for i in raw_data]

ans = 1 << 60

max_pos = max(data)

for pos in range(max_pos):
    req = 0
    for i in data:
        dist = abs(i - pos)
        cost = dist * (dist + 1) // 2
        req += cost
    ans = min(ans, req)

print(ans)
