from collections import deque

materials = list(map(int, input().split()))
magic_level = deque(map(int, input().split()))
doll = 0
wooden_train = 0
teddy_bear = 0
bicycle = 0

while materials and magic_level:
    flag = False
    if materials[-1] == 0:
        materials.pop()
        flag = True

    if magic_level[0] == 0:
        magic_level.popleft()
        flag = True

    if flag:
        continue

    material = materials.pop()
    magic = magic_level.popleft()
    if material * magic == 400:
        bicycle += 1
    elif material * magic == 300:
        teddy_bear += 1
    elif material * magic == 250:
        wooden_train += 1
    elif material * magic == 150:
        doll += 1
    elif material * magic < 0:
        sum_of_numbers = material + magic
        materials.append(sum_of_numbers)
    else:
        materials.append(material + 15)

toys = {}

if doll > 0:
    toys['Doll'] = doll
if wooden_train > 0:
    toys['Wooden train'] = wooden_train
if teddy_bear > 0:
    toys['Teddy bear'] = teddy_bear
if bicycle > 0:
    toys['Bicycle'] = bicycle

if doll > 0 and wooden_train > 0 or teddy_bear > 0 and bicycle > 0:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, reversed(materials)))}")

if magic_level:
    print(f"Magic left: {', '.join(map(str, magic_level))}")

for k, v in sorted(toys.items()):
    print(f"{k}: {v}", end="\n")