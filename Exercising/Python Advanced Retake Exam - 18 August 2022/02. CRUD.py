size = 6
matrix = []

for row in range(size):
    line = input().split()
    matrix.append(line)

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

position = list(map(int, input().strip("(").strip(")").split(", ")))

while True:
    command = input().split(', ')
    if command[0] == 'Stop':
        break

    if command[0] == 'Create':
        direction = command[1]
        row, col = [
            position[0] + directions[direction][0],
            position[1] + directions[direction][1]
        ]
        if matrix[row][col] == '.':
            matrix[row][col] = command[2]
            position = [row, col]
        else:
            continue
    elif command[0] == 'Update':
        direction = command[1]
        row, col = [
            position[0] + directions[direction][0],
            position[1] + directions[direction][1]
        ]
        if matrix[row][col] != '.':
            matrix[row][col] = command[2]
            position = [row, col]
        else:
            continue
    elif command[0] == 'Delete':
        direction = command[1]
        row, col = [
            position[0] + directions[direction][0],
            position[1] + directions[direction][1]
        ]
        if matrix[row][col] != '.':
            matrix[row][col] = '.'
            position = [row, col]
        else:
            continue
    elif command[0] == 'Read':
        direction = command[1]
        row, col = [
            position[0] + directions[direction][0],
            position[1] + directions[direction][1]
        ]
        if matrix[row][col] != '.':
            print(matrix[row][col])
            position = [row, col]
        else:
            continue

for row in matrix:
    print(*row, sep=' ')