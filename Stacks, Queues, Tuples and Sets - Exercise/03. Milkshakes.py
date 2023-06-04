from collections import deque

chocolate = list(map(int, input().split(', ')))
milk = deque(map(int, input().split(', ')))
milkshakes = 0

while milkshakes < 5 and chocolate and milk:
    flag = False
    if chocolate[-1] <= 0:
        chocolate.pop()
        flag = True

    if milk[0] <= 0:
        milk.popleft()
        flag = True

    if flag:
        continue

    if chocolate[-1] == milk[0]:
        milkshakes += 1
        chocolate.pop()
        milk.popleft()
    else:
        remove_glass = milk.popleft()
        chocolate[-1] -= 5
        milk.append(remove_glass)

if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

if chocolate:
    print(f"Chocolate: {', '.join(map(str, chocolate))}")
else:
    print("Chocolate: empty")

if milk:
    print(f"Milk: {', '.join(map(str, milk))}")
else:
    print("Milk: empty")