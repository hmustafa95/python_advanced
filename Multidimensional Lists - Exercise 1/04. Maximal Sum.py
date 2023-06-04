from sys import maxsize

rows, cols = [int(x) for x in input().split()]
matrix = []

for idx in range(rows):
    matrix.append([int(x) for x in input().split()])

biggest_square = []
biggest_sum = -maxsize

for row in range(rows - 2):
    for col in range(cols - 2):
        square = [
            list(map(int, [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]])),
            list(map(int, [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]])),
            list(map(int, [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]))
        ]
        square_sum = sum(sum(square, []))
        if square_sum > biggest_sum:
            biggest_sum = square_sum
            biggest_square = square

print(f"Sum = {biggest_sum}")
for square in biggest_square:
    print(' '.join(map(str, square)))
