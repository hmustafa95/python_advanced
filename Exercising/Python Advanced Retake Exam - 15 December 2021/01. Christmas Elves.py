from collections import deque

elves = deque(map(int, input().split()))
materials = list(map(int, input().split()))
total_energy = 0
toys = 0
counter = 0

while materials and elves:
    if elves[0] < 5:
        elves.popleft()
    if elves[0] < materials[-1]:
        elves[0] = elves[0] * 2
        elves.append(elves.popleft())
    counter += 1
    elf = elves.popleft()
    material = materials.pop()
    if counter % 3 == 0 and counter % 5 == 0:
        result = elf - (2 * material)
        if result >= 0:
            total_energy += (2 * material)
            elves.append(elf)
        else:
            elf = elf * 2
            elves.append(elf)
            materials.append(material)
    elif counter % 3 == 0 and counter % 5 != 0:
        result = elf - (2 * material)
        if result >= 0:
            toys += 2
            total_energy += (2 * material)
            elf -= (2 * material) - 1
            elves.append(elf)
        else:
            elf = elf * 2
            elves.append(elf)
            materials.append(material)
    elif counter % 5 == 0 and counter % 3 != 0:
        result = elf - material
        if result >= 0:
            total_energy += material
            elves.append(elf)
    else:
        result = elf - material
        if result >= 0:
            toys += 1
            total_energy += material
            elf -= material - 1
            elves.append(elf)

print(f"Toys: {toys}")
print(f"Energy: {total_energy}")
if elves:
    print(f"Elves left: {', '.join(map(str, elves))}")
if materials:
    print(f"Boxes left: {', '.join(map(str, materials))}")