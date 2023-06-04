size = 8
matrix = []
white_pawn_pos = []
black_pawn_pos = []

for row in range(size):
    line = input().split()
    matrix.append(line)
    if 'w' in line:
        white_pawn_pos = [row, line.index('w')]
    if 'b' in line:
        black_pawn_pos = [row, line.index('b')]

while True:
    if white_pawn_pos[0] == 0:
        print(f"Game over! White win, capture on .")
    elif black_pawn_pos[0] == size - 1:
        print(f"Game over! Black win, capture on .")
