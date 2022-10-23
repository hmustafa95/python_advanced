number = int(input())
cars = []

for index in range(number):
    command_list = input().split(', ')
    if command_list[0] == 'IN':
        if command_list[1] not in cars:
            cars.append(command_list[1])
    elif command_list[0] == 'OUT':
        if command_list[1] in cars:
            cars.remove(command_list[1])

if len(cars) > 0:
    print('\n'.join(cars))
else:
    print('Parking Lot is Empty')

# from lections below

lines = int(input())
car_plates = set()

for i in range(lines):
    direction, plate = input().split()
    if direction == 'IN':
        car_plates.add(plate)
    if direction == 'OUT':
        car_plates.remove(plate)

if len(car_plates) > 0:
    for plate in car_plates:
        print(plate)
else:
    print('Parking Lot is Empty')