# Advent of Code 2022 Day 7 : https://adventofcode.com/2022/day/7

EXPECTED_OUTPUT_FROM_DESCRIPTION = 95437

ROOT = None
TOTAL_SPACE = 70_000_000
REQUIRED_SPACE = 30_000_000


class EntityType:
    DIR = "dir"
    FILE = "file"


class Entity:
    def __init__(self, type, name):
        self.type = type
        self.name = name
        self.size = 0
        self.children = {}
        self.parent = None

    def __str__(self):
        string = ""
        string += '- ' + self.name + ' (' + self.type
        string += ')\n' if self.type == EntityType.DIR else f', size={self.size})\n'
        string += "".join([str(child) for child in self.children.values()])
        return string

    def __lt__(self, other):
        return self.size < other.size

    def add_children(self, children):
        children_entities = []
        for child in children:
            e_type, name = child.split()
            if e_type == EntityType.DIR:
                new_child = Entity(EntityType.DIR, name)
                new_child.parent = self
                children_entities.append(new_child)
            else:
                size = int(e_type)
                new_child = Entity(EntityType.FILE, name)
                new_child.size = size
                new_child.parent = self
                children_entities.append(new_child)
        self.children = \
            {child.name: child for child in children_entities}
        self.update_size(sum([c.size for c in self.children.values()]))

    def update_size(self, size):
        self.size += size
        if self.name != '/':
            self.parent.update_size(size)


def process_input(data: list):
    # process input data here
    command_and_output = []
    for i in range(len(data)):
        if data[i][0] == "$":
            output = []
            for j in range(i+1, len(data)):
                if data[j][0] == "$":
                    break
                output.append(data[j].rstrip("\n"))

            temp = [data[i].rstrip("\n"), output]
            command_and_output.append(temp)
    return command_and_output

# --- Part One ---
def part1(input_data):
    x = None
    for command, output in input_data:
        if "$ cd " in command:
            loc = command.split()[-1]
            if loc == '/':
                x = Entity(EntityType.DIR, loc)
                global ROOT
                ROOT = x
            elif loc == '..':
                x = x.parent
            else:
                x = x.children.get(loc)
        else:
            x.add_children(output)

    return sum([c.size for c in find_usefull(ROOT)])

def find_usefull(root: Entity):
    possibilities = []
    if root.size <= 100_000:
        possibilities.append(root)
    for child in root.children.values():
        if child.type == EntityType.DIR:
            possibilities += find_usefull(child)
    return possibilities

if __name__ == '__main__':
    import os

    with open(os.path.join(os.path.dirname(__file__), "test_input.txt")) as f:
        data = f.readlines()

    output = part1(process_input(data))
    print(output)
    assert output == EXPECTED_OUTPUT_FROM_DESCRIPTION

    with open(os.path.join(os.path.dirname(__file__), "input.txt"))as f:
        data = f.readlines()

    input_data = process_input(data)
    print(part1(input_data))
# Your puzzle answer was 1297159.


# --- Part Two ---

def find_usefull_2(root: Entity, size):
    possibilities = []
    if root.size > size:
        possibilities.append(root)
    for child in root.children.values():
        if child.type == EntityType.DIR:
            possibilities += find_usefull_2(child, size)
    return possibilities

def part2(input_data):

    used = ROOT.size
    free = TOTAL_SPACE - used
    to_delete = REQUIRED_SPACE - free

    return min(find_usefull_2(ROOT, to_delete)).size


if __name__ == '__main__':
    import os
    with open(os.path.join(os.path.dirname(__file__), "input.txt"))as f:
        data = f.readlines()

    input_data = process_input(data)
    print(part2(input_data))
    # Your puzzle answer was 3866390.