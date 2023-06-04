first = set(map(int, input().split()))
second = set(map(int, input().split()))
number = int(input())

for _ in range(number):
    command = input()
    if command == 'Check Subset':
        print(first.issubset(second) or second.issubset(first))
    command = command.split()
    given_numbers = set(map(int, command[2:]))
    if command[0] == 'Add':
        if command[1] == 'First':
            for idx in given_numbers:
                first.add(idx)
        elif command[1] == 'Second':
            for idx in given_numbers:
                second.add(idx)
    elif command[0] == 'Remove':
        if command[1] == 'First':
            for idx in given_numbers:
                if idx in first:
                    first.remove(idx)
        elif command[1] == 'Second':
            for idx in given_numbers:
                if idx in second:
                    second.remove(idx)

first = sorted(first)
second = sorted(second)
print(*first, sep=', ')
print(*second, sep=', ')