number = int(input())
stack = []

for idx in range(int(number)):
    command = input()
    if command[0] == '1':
        command_list = command.split()
        stack.append(int(command_list[1]))
    elif command == '2':
        if len(stack) > 0:
            stack.pop()
    elif command == '3':
        print(max(stack))
    elif command == '4':
        print(min(stack))

stack.reverse()

print(', '.join(list(map(str, stack))))