from collections import deque

bees = deque(map(int, input().split()))
nectar = list(map(int, input().split()))
symbols = deque(map(str, input().split()))
honey = 0

while bees and nectar:
    if nectar[-1] < bees[0]:
        nectar.pop()
    else:
        bee = bees.popleft()
        nectar_collected = nectar.pop()
        if symbols[0] == '+':
            honey += abs(nectar_collected + bee)
        elif symbols[0] == '-':
            honey += abs(bee - nectar_collected)
        elif symbols[0] == '*':
            honey += abs(bee - nectar_collected)
        elif symbols[0] == '/':
            if bee != 0 and nectar_collected != 0:
                honey += abs(bee // nectar_collected)
        symbols.popleft()

print(f"Total honey made: {honey}")

if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")

if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")