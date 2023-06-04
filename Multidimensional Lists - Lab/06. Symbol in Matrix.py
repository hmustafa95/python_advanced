rows = int(input())
matrix = []

for _ in range(rows):
    matrix.append(list(input()))

requested_symbol = input()

flag = False
for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == requested_symbol:
            print(f"({row}, {col})")
            flag = True
            break
    if flag:
        break

if not flag:
    print(f"{requested_symbol} does not occur in the matrix")