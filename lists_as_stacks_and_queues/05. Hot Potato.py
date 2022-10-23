kids_names = input().split()
toss = int(input())
counter = 0

while len(kids_names) > 1:
    child_turn = kids_names.pop(0)
    counter += 1
    if counter != toss:
        kids_names.append(child_turn)
    else:
        print(f'Removed {child_turn}')
        counter = 0

print(f'Last is {"".join(kids_names)}')