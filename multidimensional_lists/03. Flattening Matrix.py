rows = int(input())
matrix = []

for row in range(rows):
    cols = [int(x) for x in input().split(', ')]
    for col in cols:
        matrix.append(col)

print(matrix)