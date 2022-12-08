cwd = root = {}
stack = []

if __name__ == '__main__':
    import os
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as f:
            data = f.read()
grid = [list(map(int, line)) for line in data.splitlines()]

visible_trees = 0
for row in range(len(grid)):
    for column in range(len(grid[row])):
        tree_height = grid[row][column]

        checks = [
            all(grid[row][i] < tree_height for i in range(column)),
            all(grid[row][i] < tree_height for i in range(column + 1, len(grid[row]))),
            all(grid[i][column] < tree_height for i in range(row)),
            all(grid[i][column] < tree_height for i in range(row + 1, len(grid))),
        ]
        visible_trees += 1 if any(checks) else 0

print("Answer:", visible_trees)


total = 0
for row in range(len(grid)):
    for column in range(len(grid[row])):
        tree_height = grid[row][column]
        l, r, u, d = (0, 0, 0, 0)

        for i in range(column - 1, -1, -1):
            l += 1
            if grid[row][i] >= tree_height:
                break

        for i in range(column + 1, len(grid[row])):
            r += 1
            if grid[row][i] >= tree_height:
                break
        for i in range(row - 1, -1, -1):
            u += 1
            if grid[i][column] >= tree_height:
                break

        for i in range(row + 1, len(grid)):
            d += 1
            if grid[i][column] >= tree_height:
                break

        total = max(total, l * r * u * d)

print("Answer:", total)