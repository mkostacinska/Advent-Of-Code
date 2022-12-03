with open('./solutions/day3-input.txt') as f:
    lines = f.readlines()
lines = [line.rstrip('\n') for line in lines]

#part 1
total = 0
for line in lines:
    common = set(line[int(len(line)/2):]).intersection(line[:int(len(line)/2)])

    for l in common:
        if l.isupper():
            total+=ord(l)-64+26
        else:
            total+=ord(l)-96

print('PART1: '+str(total))

#part 2
total2 = 0
for i in range(0, len(lines), 3):
    common = set(lines[i]).intersection(lines[i+1]).intersection(lines[i+2])
    for l in common:
        if l.isupper():
            total2+=ord(l)-64+26
        else:
            total2+=ord(l)-96
print('PART2: '+str(total2))
   