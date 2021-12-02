with open('data.txt') as f:
    data = f.read()

data_arr = data.split('\n')

# ------------- First part --------------
depth = 0
horizontal_pos = 0

for position in data_arr:
    direction = position.split(' ')
    if direction[0] == 'forward':
        horizontal_pos += int(direction[1])
    elif direction[0] == 'up':
        depth -= int(direction[1])
    elif direction[0] == 'down':
        depth += int(direction[1])

print(
    f'Horizontal position {horizontal_pos} multiplied by depth {depth} = {horizontal_pos*depth}'
    )


# ----------------- Second part -------------------
depth = 0
horizontal_pos = 0
aim = 0
for position in data_arr:
    direction = position.split(' ')
    if direction[0] == 'forward':
        horizontal_pos += int(direction[1])
        depth = depth + aim * int(direction[1])
    elif direction[0] == 'up':
        aim = aim - int(direction[1])
    elif direction[0] == 'down':
        aim += int(direction[1])

print(
    f'Horizontal position {horizontal_pos} multiplied by depth {depth} = {horizontal_pos*depth}'
    )

