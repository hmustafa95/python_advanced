rows = int(input())
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

primary_diagonal = 0
primary = []
secondary_diagonal = 0
secondary = []
for idx in range(rows):
    primary_diagonal += matrix[idx][idx]
    primary.append(matrix[idx][idx])
    secondary_diagonal += matrix[idx][rows - idx - 1]
    secondary.append(matrix[idx][rows - idx - 1])

print(f"Primary diagonal: {', '.join(map(str, primary))}. Sum: {primary_diagonal}")
print(f"Secondary diagonal: {', '.join(map(str, secondary))}. Sum: {secondary_diagonal}")