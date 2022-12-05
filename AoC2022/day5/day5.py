# Advent of Code 2022 Day 1 : https://adventofcode.com/2022/day/1

##################### Instructions #####################
# --- Day 5: Supply Stacks ---
# The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

# The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

# The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

# They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2
# In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

# Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

# [D]        
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
# In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

#         [Z]
#         [N]
#     [C] [D]
#     [M] [P]
#  1   2   3
# Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

#         [Z]
#         [N]
# [M]     [D]
# [C]     [P]
#  1   2   3
# Finally, one crate is moved from stack 1 to stack 2:

#         [Z]
#         [N]
#         [D]
# [C] [M] [P]
#  1   2   3
# The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

# After the rearrangement procedure completes, what crate ends up on top of each stack?

##################### Solution #####################
from pprint import pprint
EXPECTED_OUTPUT_FROM_DESCRIPTION = 'CMZ'


def process_input(data: list):
    # process input data here
    stacks = [[] for i in range(len(data[0])//4)]
    instructions = []
    done_collecting_stacks = False
    for i in data:
        i = i.rstrip('\n')
        if i == '':
            done_collecting_stacks = True
            continue
        if done_collecting_stacks:
            strings = i.split()
            inst = []
            for j in range(len(strings)):
                if j % 2 == 0:
                    continue
                inst.append(int(strings[j]))
            instructions.append(inst)
        else:
            string = i.replace("    ", "  ").replace('[', "").replace(']', "")
            for j in range(len(string)):
                if j % 2 != 0:
                    continue
                if string[j] != ' ':
                    stacks[j//2].append(string[j])
    return (stacks, instructions)


def part1(input_data):
    stacks, instructions = input_data
    for instruction in instructions:
        quantity, form_stack, to_stack = instruction
        for i in range(quantity):
            val = stacks[form_stack-1].pop(0)
            stacks[to_stack-1].insert(0, val)
    return ''.join([stack.pop(0) for stack in stacks])

if __name__ == '__main__':
    import os

    with open(os.path.join(os.path.dirname(__file__), "test_input.txt")) as f:
        data = f.readlines()

    output = part1(process_input(data))
    print(output)
    assert output == EXPECTED_OUTPUT_FROM_DESCRIPTION

    with open(os.path.join(os.path.dirname(__file__), "input.txt"))as f:
        data = f.readlines()

    print(part1(process_input(data)))
# Your puzzle answer was SPFMVDTZT.

# --- Part Two ---
##################### Instructions #####################
# As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

# Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

# The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

# Again considering the example above, the crates begin in the same configuration:

#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
# Moving a single crate from stack 2 to stack 1 behaves the same as before:

# [D]        
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
# However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

#         [D]
#         [N]
#     [C] [Z]
#     [M] [P]
#  1   2   3
# Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

#         [D]
#         [N]
# [C]     [Z]
# [M]     [P]
#  1   2   3
# Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

#         [D]
#         [N]
#         [Z]
# [M] [C] [P]
#  1   2   3
# In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

# Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?
##################### Solution #####################

def part2(input_data):
    stacks, instructions = input_data
    for instruction in instructions:
        quantity, form_stack, to_stack = instruction
        temp_vals = stacks[form_stack-1][:quantity]
        stacks[form_stack-1] = stacks[form_stack-1][quantity:]
        stacks[to_stack-1] = temp_vals + stacks[to_stack-1]
    return ''.join([stack.pop(0) for stack in stacks])


if __name__ == '__main__':
    import os
    with open(os.path.join(os.path.dirname(__file__), "input.txt"))as f:
        data = f.readlines()

    print(part2(process_input(data)))
# Your puzzle answer was ZFSJBPRFP.