with open('./solutions/inputs/day1-input.txt') as f:
    lines = f.readlines()

# PART 1 solution - explicitly summing up
current = 0
all = []
for line in lines:
    if line == '\n':
        all.append(current)
        current = 0
        continue
    current += int(line.rstrip('\n'))

print('PART1: ' + str(max(all)))

# PART 2 solution:
print('PART2: '+str(sum(list(reversed(sorted(all)))[:3])))