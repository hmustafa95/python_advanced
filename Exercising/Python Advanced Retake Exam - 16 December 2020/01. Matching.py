from collections import deque

males = list(map(int, input().split()))
females = deque(map(int, input().split()))
matches = 0

while males and females:
    male = males.pop()
    if male <= 0:
        continue
    female = females.popleft()
    if female <= 0:
        males.append(male)
        continue
    if male % 25 == 0:
        females.insert(0, female)
        males.pop()
        continue
    if female % 25 == 0:
        males.append(male)
        females.popleft()
        continue
    if male == female:
        matches += 1
    else:
        male = male - 2
        males.append(male)

print(f"Matches: {matches}")

if males:
    print(f"Males left: {', '.join(map(str, males[::-1]))}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join(map(str, females))}")
else:
    print("Females left: none")