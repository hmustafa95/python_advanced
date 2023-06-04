size = int(input())
matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

while True:
    command = input().split()
    if command[0] == 'END':
        break
    points = [int(x) for x in command[1:]]
    if command[0] == 'Add':
        if 0 <= points[0] <= (size - 1) and 0 <= points[1] <= (size - 1):
            matrix[points[0]][points[1]] += points[2]
        else:
            print('Invalid coordinates')
            continue
    elif command[0] == 'Subtract':
        if 0 <= points[0] <= (size - 1) and 0 <= points[1] <= (size - 1):
            matrix[points[0]][points[1]] -= points[2]
        else:
            print('Invalid coordinates')

for row in matrix:
    print(' '.join(map(str, row)))