size = int(input())
matrix = []

for _ in range(size):
    matrix.append(list(input().split(', ')))

primary = 0
primary_list = []
secondary = 0
secondary_list = []

for row in range(size):
    primary += int(matrix[row][row])
    primary_list.append(matrix[row][row])
    secondary += int(matrix[row][size - row - 1])
    secondary_list.append(matrix[row][size - row - 1])

print(f"Primary diagonal: {', '.join(primary_list)}. Sum: {primary}")
print(f"Secondary diagonal: {', '.join(secondary_list)}. Sum: {secondary}")