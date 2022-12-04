with open('./solutions/day4-input.txt') as f:
    lines = f.readlines()
lines = [line.rstrip('\n') for line in lines]

# PART 1
contained = 0
for line in lines:
    elves = [list(int(vals) for vals in value.split('-')) for value in line.split(',')]
    if (elves[0][0]>= elves[1][0] and elves[0][1]<=elves[1][1]) or (elves[0][0]<= elves[1][0] and elves[0][1]>=elves[1][1]):
        contained += 1

print('PART1: '+str(contained))

# PART 2
overlapped = 0
for line in lines:
    elves = [list(int(vals) for vals in value.split('-')) for value in line.split(',')]
    # reshuffle
    if elves[0][0] >= elves [1][0]:
        elves[0], elves[1] = elves[1], elves[0]
    # check if bounds overlapping
    if elves[0][1] >= elves [1][0]:
        overlapped += 1
print('PART2: '+str(overlapped))

