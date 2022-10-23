stack = []
number = int(input())

for index in range(number):
    command = input()
    if '1' in command:
        command_list = command.split()
        stack.append(int(command_list[1]))
    elif command == '2':
        if stack:
            stack.pop()
    elif command == '3':
        if stack:
            print(max(stack))
    elif command == '4':
        if stack:
            print(min(stack))

stack_length = len(stack)
for index in range(stack_length):
    spacing = ', ' if index < stack_length - 1 else ''
    print(str(stack.pop()) + spacing, end='')