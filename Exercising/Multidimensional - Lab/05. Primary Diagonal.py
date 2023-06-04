size = int(input())
matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

primary = 0

for row in range(size):
    primary += matrix[row][row]

print(primary)