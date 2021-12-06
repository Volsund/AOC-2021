with open('data.txt') as f:
    data = f.read().splitlines()

line_coords = []
for line in data:
    dirty_line = line.split()
    dirty_line.pop(1)
    first_dot = dirty_line[0].split(',')
    second_dot = dirty_line[1].split(',')
    new_line = []
    new_line.append(int(first_dot[0]))
    new_line.append(int(first_dot[1]))
    new_line.append(int(second_dot[0]))
    new_line.append(int(second_dot[1]))
    line_coords.append(new_line)

max_coord = 0
for line in line_coords:
    for num in line:
        if num > max_coord:
            max_coord = num

diagram = []
for i in range(max_coord + 1):
    row = []
    for i in range(max_coord + 1):
        row.append(0)
    diagram.append(row)

for line in line_coords:
    if line[0] == line[2]:  # Line is vertical
        if line[1] < line[3]:
            for i in range(line[1], line[3]+1):
                diagram[i][line[0]] += 1
        else:
            for i in range(line[3], line[1]+1):
                diagram[i][line[0]] += 1

    elif line[1] == line[3]:  # Line is horizontal
        if line[0] < line[2]:
            for num in range(line[0], line[2]+1):
                diagram[line[1]][num] += 1
        else:
            for num in range(line[2], line[0]+1):
                diagram[line[1]][num] += 1

    else:  # Line is diagonal -- Part 2
        if line[0] > line[2]:
            y = line[3]
            for i in range(line[2], line[0]+1):
                diagram[y][i] += 1
                if line[1] < line[3]:
                    y -= 1
                else:
                    y += 1
        elif line[0] < line[2]:
            y = line[1]
            for i in range(line[0], line[2]+1):
                diagram[y][i] += 1
                if line[1] < line[3]:
                    y += 1
                else:
                    y -= 1

for row in diagram:
    print(row)

counter = 0
for row in diagram:
    for num in row:
        if num >= 2:
            counter += 1

print(f'Points where at least 2 lines overlap: {counter}')
