from collections import deque

seats = list(map(str, input().split(', ')))
first = deque(map(int, input().split(', ')))
second = list(map(int, input().split(', ')))
taken_seats = []
rotations = 0

while True:
    if rotations == 10:
        break
    if len(taken_seats) == 3:
        break
    rotations += 1
    first_number = first.popleft()
    second_number = second.pop()
    result = first_number + second_number
    letter = chr(result)
    seat_first = str(first_number) + letter
    seat_second = str(second_number) + letter
    for current_seat in [seat_first, seat_second]:
        if current_seat in taken_seats:
            break
        if current_seat in seats:
            seats.remove(current_seat)
            taken_seats.append(current_seat)
            break
    else:
        first.append(first_number)
        second.insert(0, second_number)

print(f"Seat matches: {', '.join(taken_seats)}")
print(f"Rotations count: {rotations}")