if __name__ == '__main__':
    import os
    with open(os.path.join(os.path.dirname(__file__), "input.txt"))as f:
        data = [int(i) for i in f.read().strip().split("\n")]

N = len(data)

count = 0  # Number of increasing depths

for i in range(1, N):
    if data[i] > data[i - 1]:
        count += 1

print(count)
