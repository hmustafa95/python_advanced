first_stack = set(map(int, input().split()))
second_stack = set(map(int, input().split()))
number = int(input())

for i in range(number):
    command = input().split()
    math_problem = command[0]
    position = command[1]
    if math_problem == 'Add':
        if position == 'First':
            for index in command[2:]:
                first_stack.add(int(index))
        elif position == 'Second':
            for index in command[2:]:
                second_stack.add(int(index))
    elif math_problem == 'Remove':
        if position == 'First':
            for index in command[2:]:
                if int(index) in first_stack:
                    first_stack.remove(int(index))
        elif position == 'Second':
            for index in command[2:]:
                if int(index) in second_stack:
                    second_stack.remove(int(index))
    else:
        print(first_stack.issubset(second_stack) or second_stack.issubset(first_stack))

print(', '.join(map(str, sorted(map(int, {i for i in first_stack})))))
print(', '.join(map(str, sorted(map(int, {i for i in second_stack})))))
