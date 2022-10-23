que = []

while True:
    name = input()
    if name == 'End':
        print(f'{len(que)} people remaining.')
        break
    elif name == 'Paid':
        while len(que) > 0:
            print(f'{que.pop(0)}')
    else:
        que.append(name)