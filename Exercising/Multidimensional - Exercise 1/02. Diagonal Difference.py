size = int(input())
matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

primary = 0
secondary = 0

for idx in range(size):
    primary += matrix[idx][idx]
    secondary += matrix[idx][size - idx - 1]

result = abs(primary - secondary)
print(result)