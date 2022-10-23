from collections import deque

bees = deque(map(int, input().split()))
nectar = list(map(int, input().split()))
symbols = deque(input().split())
total_honey = 0

while bees and nectar:
    if nectar[-1] >= bees[0]:
        bee = bees.popleft()
        collected_nectar = nectar.pop()
        symbol = symbols.popleft()
        if symbol == '+':
            total_honey += abs(bee + collected_nectar)
        elif symbol == '-':
            total_honey += abs(bee - collected_nectar)
        elif symbol == '*':
            total_honey += abs(bee * collected_nectar)
        elif symbol == '/':
            if bee != 0 and collected_nectar != 0:
                total_honey += abs(bee / collected_nectar)
    else:
        nectar.pop()

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")