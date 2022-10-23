quantity = int(input())
que = []

while True:
    name = input()
    if name == 'Start':
        break
    else:
        que.append(name)

while True:
    command = input()
    if command == 'End':
        print(f'{quantity} liters left')
        break
    command_list = command.split()
    if len(command_list) == 1:
        requested_liters = int(command_list[0])
        if quantity >= requested_liters:
            print(f'{que[0]} got water')
            que.pop(0)
            quantity -= requested_liters
        else:
            print(f'{que[0]} must wait')
            que.pop(0)
    else:
        quantity += int(command_list[1])