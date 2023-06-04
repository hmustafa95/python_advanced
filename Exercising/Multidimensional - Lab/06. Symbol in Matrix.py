size = int(input())
matrix = []

for _ in range(size):
    matrix.append(list(input()))

symbol = input()

rowy, coly = 0, 0
flag = False
for row in range(size):
    for col in range(row):
        if symbol == matrix[row][col]:
            flag = True
            rowy = row
            coly = col

if flag:
    print(f"({rowy}, {coly})")
else:
    print(f"{symbol} does not occur in matrix")
