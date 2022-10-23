rows = int(input())
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

diagonal = 0
for idx in range(rows):
    diagonal += matrix[idx][idx]

print(diagonal)