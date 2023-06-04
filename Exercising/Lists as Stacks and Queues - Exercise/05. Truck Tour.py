from collections import deque

petrol_pumps = deque()
petrol_pumps_count = int(input())

for _ in range(petrol_pumps_count):
    amount_petrol, distance_to_pump = input().split()
    petrol_pumps.append([int(amount_petrol), int(distance_to_pump)])

for attempt in range(petrol_pumps_count):
    current_level_petrol = 0
    is_failed = False
    for petrol_amount, distance in petrol_pumps:
        current_level_petrol += petrol_amount
        if current_level_petrol < distance:
            is_failed = True
            break
        else:
            current_level_petrol -= distance
    if is_failed:
        petrol_pumps.append(petrol_pumps.popleft())
    else:
        print(attempt)
        break