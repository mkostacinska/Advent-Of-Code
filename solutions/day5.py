crates = [
    ['T', 'P', 'Z', 'C', 'S', 'L', 'Q', 'N'],
    ['L', 'P', 'T', 'V', 'H', 'C', 'G'],
    ['D', 'C', 'Z', 'F'],
    ['G', 'W', 'T', 'D', 'L', 'M', 'V', 'C'],
    ['P', 'W', 'C'],
    ['P', 'F', 'J', 'D', 'C', 'T', 'S', 'Z'],
    ['V', 'W', 'G', 'B', 'D'],
    ['N', 'J', 'S', 'Q', 'H', 'W'],
    ['R', 'C', 'Q', 'F', 'S', 'L', 'V'],
]

crates2 = [
    ['T', 'P', 'Z', 'C', 'S', 'L', 'Q', 'N'],
    ['L', 'P', 'T', 'V', 'H', 'C', 'G'],
    ['D', 'C', 'Z', 'F'],
    ['G', 'W', 'T', 'D', 'L', 'M', 'V', 'C'],
    ['P', 'W', 'C'],
    ['P', 'F', 'J', 'D', 'C', 'T', 'S', 'Z'],
    ['V', 'W', 'G', 'B', 'D'],
    ['N', 'J', 'S', 'Q', 'H', 'W'],
    ['R', 'C', 'Q', 'F', 'S', 'L', 'V'],
]

with open('./solutions/inputs/day5-input.txt') as f:
    lines = f.readlines()
lines = [line.rstrip('\n') for line in lines]

# PART 1
for step in lines:
    l = step.lstrip('move ').split(' ')
    amount, start, end = int(l[0]), int(l[2])-1, int(l[4])-1
    for i in range(amount):
        crate = crates[start][-1]
        crates[end].append(crate)
        del crates[start][-1]

print('PART 1: ', end='')
for stack in crates:
    print(stack[-1], end='')
print()

# PART2:
for step in lines:
    l = step.lstrip('move ').split(' ')
    amount, start, end = int(l[0]), int(l[2])-1, int(l[4])-1
    to_move = []
    for i in range(amount):
        crate = crates2[start][-1]
        to_move.insert(0, crate)
        del crates2[start][-1]
    crates2[end].extend(to_move)

print('PART 2: ', end='')
for stack in crates2:
    print(stack[-1], end='')
print()