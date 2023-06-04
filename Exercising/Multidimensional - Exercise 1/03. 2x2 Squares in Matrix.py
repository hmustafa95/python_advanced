rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append([x for x in input().split()])

matches = 0
for row in range(rows):
    for col in range(cols):
        if (row + 1) < rows and (col + 1) < cols:
            if matrix[row][col] == matrix[row][col + 1] and matrix[row][col] == matrix[row + 1][col] and matrix[row][col] == matrix[row +1][col + 1]:
                matches += 1

print(matrix)