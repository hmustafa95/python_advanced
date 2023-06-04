from collections import deque

chocolates = list(map(int, input().split(', ')))
cups_of_milk = deque(map(int, input().split(', ')))
milkshakes = 0

while True:
    flag = False
    if not chocolates or not cups_of_milk or milkshakes == 5:
        break
    if chocolates[-1] <= 0:
        chocolates.pop()
        flag = True
    if cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
        flag = True
    if flag:
        continue
    if chocolates[-1] == cups_of_milk[0]:
        milkshakes += 1
        chocolates.pop()
        cups_of_milk.popleft()
    else:
        cups_of_milk.append(cups_of_milk.popleft())
        chocolates[-1] -= 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(list(map(str, chocolates)))}")
else:
    print('Chocolate: empty')

if cups_of_milk:
    print(f"Milk: {', '.join(list(map(str, cups_of_milk)))}")
else:
    print('Milk: empty')