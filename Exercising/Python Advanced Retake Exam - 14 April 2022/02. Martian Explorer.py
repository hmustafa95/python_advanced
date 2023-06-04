size = 6
matrix = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

start_pos = []

for row in range(size):
    line = input().split()
    matrix.append(line)
    if 'E' in line:
        start_pos = [row, line.index('E')]

move_list = input().split(', ')

water_deposit = 0
metal_deposit = 0
concrete_deposit = 0

for move in move_list:
    row, col = [
        start_pos[0] + directions[move][0],
        start_pos[1] + directions[move][1]
    ]
    start_pos[0] += directions[move][0]
    start_pos[1] += directions[move][1]
    if row < 0:
        row = size + row
        start_pos[0] = row
    elif row >= size:
        row = 0
    if col < 0:
        col = size + col
        start_pos[1] = col
    elif col >= size:
        col = 0

    if matrix[row][col] == 'R':
        print(f"Rover got broken at ({row}, {col})")
        break

    elif matrix[row][col] == 'W':
        print(f"Water deposit found at ({row}, {col})")
        water_deposit += 1

    elif matrix[row][col] == 'M':
        print(f"Metal deposit found at ({row}, {col})")
        metal_deposit += 1

    elif matrix[row][col] == 'C':
        print(f"Concrete deposit found at ({row}, {col})")
        concrete_deposit += 1

if water_deposit > 0 and metal_deposit > 0 and concrete_deposit > 0:
    print('Area suitable to start the colony.')
else:
    print('Area not suitable to start the colony.')