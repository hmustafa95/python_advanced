size = int(input())
matrix = []

for row in range(size):
    matrix.append([int(x) for x in input().split(', ') if int(x) % 2 == 0])

print(matrix)