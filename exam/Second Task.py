size = int(input())
matrix = []
race_car = input()
location_race_car = [0, 0]
tunnel_locations = {'T': []}
km_driven = 0

for idx in range(size):
    line = input().split()
    matrix.append(line)
    if 'T' in line:
        tunnel_locations['T'].append([idx, line.index('T')])

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    direction = input()
    if direction == 'End':
        print(f"Racing car {race_car} DNF.")
        break
    row, col = [
        location_race_car[0] + directions[direction][0],
        location_race_car[1] + directions[direction][1]
    ]
    location_race_car[0] += directions[direction][0]
    location_race_car[1] += directions[direction][1]
    if matrix[row][col] == '.':
        km_driven += 10
    elif matrix[row][col] == 'T':
        matrix[row][col] = '.'
        list_of_rowcol = [row, col]
        tunnel_locations['T'].remove(list_of_rowcol)
        location_race_car[0] = tunnel_locations['T'][0][0]
        location_race_car[1] = tunnel_locations['T'][0][1]
        matrix[tunnel_locations['T'][0][0]][tunnel_locations['T'][0][1]] = '.'
        km_driven += 30
    elif matrix[row][col] == 'F':
        km_driven += 10
        print(f"Racing car {race_car} finished the stage!")
        break

matrix[location_race_car[0]][location_race_car[1]] = 'C'

print(f"Distance covered {km_driven} km.")
for row in matrix:
    print(''.join(row))
