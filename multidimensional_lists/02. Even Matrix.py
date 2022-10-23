number = int(input())
matrix = []

for index in range(number):
    matrix.append([int(x) for x in input().split(', ') if int(x) % 2 == 0])

print(matrix)