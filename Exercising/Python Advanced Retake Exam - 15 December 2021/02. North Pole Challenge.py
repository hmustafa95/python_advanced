rows, cols = list(map(int, input().split(', ')))
matrix = []
santa_pos = []
decorations_collected = 0
gifts_collected = 0
cookies_collected = 0
items_on_board = 0

for row in range(rows):
    line = input().split()
    matrix.append(line)
    if 'Y' in line:
        santa_pos = [row, line.index('Y')]
    for item in line:
        if item != 'Y' and item != '.':
            items_on_board += 1

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

matrix[santa_pos[0]][santa_pos[1]] = 'x'
red = []
col = []
while True:
    command = input()
    if command == 'End':
        break
    if items_on_board == 0:
        break
    direction, steps = command.split('-')
    for times in range(int(steps)):
        if items_on_board == 0:
            print('Merry Christmas!')
            break
        red, col = [
            santa_pos[0] + directions[direction][0],
            santa_pos[1] + directions[direction][1]
        ]
        santa_pos[0] += directions[direction][0]
        santa_pos[1] += directions[direction][1]
        if red < 0:
            red = rows + red
            santa_pos[0] = red
        elif red >= rows:
            red = 0
            santa_pos[0] = red
        elif col < 0:
            col = cols + col
            santa_pos[1] = col
        elif col >= cols:
            col = 0
            santa_pos[1] = col
        if matrix[red][col] == 'D':
            decorations_collected += 1
            items_on_board -= 1
        elif matrix[red][col] == 'G':
            gifts_collected += 1
            items_on_board -= 1
        elif matrix[red][col] == 'C':
            cookies_collected += 1
            items_on_board -= 1
        matrix[red][col] = 'x'

matrix[red][col] = 'Y'

print("You've collected:")
print(f'- {decorations_collected} Christmas decorations')
print(f'- {gifts_collected} Gifts')
print(f'- {cookies_collected} Cookies')
for red in matrix:
    print(*red, sep=' ')