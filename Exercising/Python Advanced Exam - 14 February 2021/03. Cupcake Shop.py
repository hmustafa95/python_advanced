from collections import deque

def stock_availability(inventory, action, *args):
    inventory = deque(inventory)
    if action == 'delivery':
        for item in args:
            inventory.append(item)
        return list(inventory)
    elif action == 'sell':
        if len(args) == 0:
            inventory.popleft()
            return list(inventory)
        elif isinstance(args[0], int):
            for idx in range(args[0]):
                inventory.popleft()
            return list(inventory)
        else:
            for idx in args:
                while idx in inventory:
                    inventory.remove(idx)
            return list(inventory)
