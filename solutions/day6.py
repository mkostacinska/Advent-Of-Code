with open('./solutions/inputs/day6-input.txt') as f:
    lines = f.readlines()
lines = [line.rstrip('\n') for line in lines]
lines = lines[0]

processing = []
output = -1
for i in range(len(lines)):
    character = lines[i]
    
    if len(processing) < 3:
        processing.append(character)

    if len(processing) == 3:
        processing.append(character)
        if len(set(processing)) == 4:
            output = i + 1
            break
    if len(processing) > 3:
        del processing[0]
        processing.append(character)
        if len(set(processing)) == 4:
            output = i + 1
            break
    
print(f'PART1: {output}')

processing = []
output = -1
for i in range(len(lines)):
    character = lines[i]
    
    if len(processing) < 13:
        processing.append(character)

    if len(processing) == 13:
        processing.append(character)
        if len(set(processing)) == 14:
            output = i + 1
            break
    if len(processing) > 13:
        del processing[0]
        processing.append(character)
        if len(set(processing)) == 14:
            output = i + 1
            break

print(f'PART2: {output}')