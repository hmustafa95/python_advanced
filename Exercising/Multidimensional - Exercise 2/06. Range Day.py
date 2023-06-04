size = 5
my_pos = []
targets_shot = 0
matrix = []

for row in range(size):
    line = input().split()
    matrix.append(line)
    if 'A' in line:
        my_pos = [row, line.index('A')]

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

targets = int(input())

for direction, position in directions.items():
    row = [my_pos[0] + directions[direction][0]]
    col = [my_pos[1] + directions[direction][1]]
