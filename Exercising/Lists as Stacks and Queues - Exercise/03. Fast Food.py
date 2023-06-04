from collections import deque

quantity = int(input())
orders = deque(map(int, input().split()))

print(max(orders))

while orders:
    if quantity >= orders[0]:
        quantity -= orders.popleft()
    else:
        break

if not orders:
    print('Orders complete')
else:
    print(f"Orders left: {' '.join(list(map(str, orders)))}")
