from collections import deque

orders = deque(map(int, input().split(', ')))
employees = list(map(int, input().split(', ')))
total_pizzas = 0

while orders and employees:
    order = orders.popleft()
    if order > 10:
        continue
    if order <= 0:
        continue
    employee = employees.pop()
    if order <= employee:
        total_pizzas += order
    else:
        remaining_pizza = order - employee
        while remaining_pizza > 0:
            if employees:
                follow_up_employee = employees.pop()
                remaining_pizza -= follow_up_employee
            else:
                orders.insert(0, remaining_pizza)
                break
        else:
            total_pizzas += order

if orders:
    print(f"Not all orders are completed.\nOrders left: {', '.join(map(str, orders))}")
else:
    print(f"All orders are successfully completed!\nTotal pizzas made: {total_pizzas}\nEmployees: {', '.join(map(str, employees))}")