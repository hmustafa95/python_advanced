rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append([x for x in input().split()])

while True:
    command = input().split()
    if command[0] == 'END':
        break
    if command[0] == 'swap':
        points = [int(x) for x in command[1:]]
        if len(points) == 4:
            if 0 <= points[0] <= rows and 0 <= points[2] <= rows and 0 <= points[1] <= cols and 0 <= points[3] <= cols:
                matrix[points[0]][points[1]], matrix[points[2]][points[3]] = matrix[points[2]][points[3]], matrix[points[0]][points[1]]
                for row in matrix:
                    print(*row, sep=' ')
            else:
                print('Invalid input!')
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')
