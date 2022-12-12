from collEctions import deque #Double end queue in really useful is this problem 
if __name__ == '__main__':
    import os

    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
        data = f.read()
grille = [list(x) for x in data.strip().splitlines()]

for rowb, row in enumerate(grille):
    for col, item in enumerate(row):
        if item == "S":
            Sr = rowb
            Sc = col
            grille[rowb][col] = "a"
        if item == "E":
            Er = rowb
            Ec = col
            grille[rowb][col] = "z"

queue = deque()
queue.append((0, Sr, Sc))

xyz = {(Sr, Sc)}

while queue:
    d, r, c = queue.popleft()
    for Nr, Nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if Nr < 0 or Nc < 0 or Nr >= len(grille) or Nc >= len(grille[0]):
            continue
        if (Nr, Nc) in xyz:
            continue
        if ord(grille[Nr][Nc]) - ord(grille[r][c]) > 1:
            continue
        if Nr == Er and Nc == Ec:
            print(d + 1)
            exit(0)
        xyz.add((Nr, Nc))
        queue.append((d + 1, Nr, Nc))



grille = [list(x) for x in data.strip().splitlines()]

for rowb, row in enumerate(grille):
    for col, item in enumerate(row):
        if item == "S":
            grille[rowb][col] = "a"
        if item == "E":
            Er = rowb
            Ec = col
            grille[rowb][col] = "z"

queue = deque()
queue.append((0, Er, Ec))

xyz = {(Er, Ec)}

while queue:
    d, r, c = queue.popleft()
    for Nr, Nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if Nr < 0 or Nc < 0 or Nr >= len(grille) or Nc >= len(grille[0]):
            continue
        if (Nr, Nc) in xyz:
            continue
        if ord(grille[Nr][Nc]) - ord(grille[r][c]) < -1:
            continue
        if grille[Nr][Nc] == "a":
            print(d + 1)
            exit(0)
        xyz.add((Nr, Nc))
        queue.append((d + 1, Nr, Nc))