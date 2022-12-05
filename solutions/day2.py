with open('./solutions/inputs/day2-input.txt') as f:
    lines = f.readlines()

lines = [line.rstrip('\n') for line in lines]

# PART1: what a beauty
key = {'Y': ['C', 'B', 'A'], 'X': ['B', 'A', 'C'], 'Z': ['A', 'C', 'B']}
value = {'X': 1, 'Y': 2, 'Z': 3}

score = sum([value[string[2]]+(key[string[2]].index(string[0])*3) for string in lines])
print(score)

# PART2: i had the key flipped for so lnd :(
key2 = {'A': ['C', 'A', 'B'], 'B': ['A', 'B', 'C'], 'C': ['B', 'C', 'A']}
value2 = {'A': 1, 'B': 2, 'C': 3}
score2 = 0
for line in lines:
    if line[2] == 'X':
        score2 += 0 + value2[key2[line[0]][0]]
    elif line[2] == 'Y':
        score2 += 3 + value2[key2[line[0]][1]]
    elif line[2] == 'Z':
        score2 += 6 + value2[key2[line[0]][2]]

print(score2)
    

