rows, cols = [int(x) for x in input().split()]
first_letter = 97

for row in range(rows):
    submatrix = []
    for col in range(cols):
        result = chr(first_letter + row) + chr(first_letter + col + row) + chr(first_letter + row)
        submatrix.append(result)
    print(*submatrix)