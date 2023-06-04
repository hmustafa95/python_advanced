import math

size = int(input())
matrix = []
player_location = []
coins_collected = 0
path = []
start_location = []

for row in range(size):
    line = input().split()
    matrix.append(line)
    if 'P' in line:
        player_location = [row, line.index('P')]
        start_location = [row, line.index('P')]

path.append(start_location)
matrix[player_location[0]][player_location[1]] = '0'

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    if coins_collected >= 100:
        break
    direction = input()
    if direction in directions:
        row, col = [
            player_location[0] + directions[direction][0],
            player_location[1] + directions[direction][1]
        ]
        player_location[0] += directions[direction][0]
        player_location[1] += directions[direction][1]
        if row < 0:
            row = size + row
            player_location[0] = row
        elif row >= size:
            row = 0
            player_location[0] = row
        elif col < 0:
            col = size + col
            player_location[1] = col
        elif col >= size:
            col = 0
            player_location[1] = col
        path.append([row, col])
        if matrix[row][col].isdigit():
            coins_collected += int(matrix[row][col])
            matrix[row][col] = '0'
        elif matrix[row][col] == 'X':
            if coins_collected > 0:
                coins_collected = math.floor(coins_collected / 2)
            break

if coins_collected >= 100:
    print(f"You won! You've collected {coins_collected} coins.")
else:
    print(f"Game over! You've collected {coins_collected} coins.")

print(f"Your path:")
for row in path:
    print(row)