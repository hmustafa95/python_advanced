size = 6
matrix = []

for row in range(size):
    line = input().split()
    matrix.append(line)

score = 0

for number_throw in range(3):
    throw = list(map(int, input().strip('(').strip(')').split(', ')))
    if size <= throw[0] or throw[0] < 0 or throw[1] >= size or throw[1] < 0:
        continue

    if matrix[throw[0]][throw[1]] == 'B':
        matrix[throw[0]][throw[1]] = 0
        for row in range(size):
            if matrix[row][throw[1]] != 'B':
                score += int(matrix[row][throw[1]])
    else:
        score += int(matrix[throw[0]][throw[1]])

needed_points = 100 - score

if score > 299:
    print(f"Good job! You scored {score} points, and you've won Lego Construction Set.")
elif 300 > score > 199:
    print(f"Good job! You scored {score} points, and you've won Teddy Bear.")
elif 200 > score > 99:
    print(f"Good job! You scored {score} points, and you've won Football.")
else:
    print(f"Sorry! You need {needed_points} points more to win a prize.")