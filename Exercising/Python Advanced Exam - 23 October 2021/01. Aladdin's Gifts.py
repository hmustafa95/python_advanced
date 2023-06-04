from collections import deque

presents = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0
}

def present(result):
    global presents
    if 100 <= result <= 199:
        presents['Gemstone'] += 1
        return
    elif 200 <= result <= 299:
        presents['Porcelain Sculpture'] += 1
        return
    elif 300 <= result <= 399:
        presents['Gold'] += 1
        return
    elif 400 <= result <= 499:
        presents['Diamond Jewellery'] += 1
        return

materials = list(map(int, input().split()))
magic_level = deque(map(int, input().split()))

while magic_level and materials:
    material = materials.pop()
    magic = magic_level.popleft()
    result = material + magic
    if result < 100:
        if result % 2 == 0:
            result = 2 * material + 3 * magic
        else:
            result = 2 * result
    if result > 499:
        result = result // 2
    if 100 <= result <= 499:
        present(result)

if presents['Gemstone'] >= 1 and presents['Porcelain Sculpture'] >= 1 or presents['Gold'] >= 1 and presents['Diamond Jewellery'] >= 1:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")

if magic_level:
    print(f"Magic left: {', '.join(map(str, magic_level))}")

for k, v in sorted(presents.items()):
    if v >= 1:
        print(f"{k}: {v}")
