size = int(input())
matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

while True:
    command = input()
    if command == 'END':
        break
    command = command.split()
    if len(command) != 4:
        print('Invalid coordinates')
        continue
    points = [int(x) for x in command[1:]]
    if not points[0] in range(0, len(matrix)) or not points[1] in range(0, len(matrix)):
        print('Invalid coordinates')
        continue

    if command[0] == 'Add':
        matrix[points[0]][points[1]] += points[2]
    elif command[0] == 'Subtract':
        matrix[points[0]][points[1]] -= points[2]

for row in matrix:
    print(*row)