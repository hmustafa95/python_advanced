from collections import deque

textiles = deque(map(int, input().split(' ')))
medicaments = list(map(int, input().split(' ')))
items = {"Patch": 0, "Bandage": 0, "MedKit": 0}

while textiles and medicaments:
    cloth = textiles.popleft()
    pill = medicaments.pop()
    sum_both = cloth + pill

    if sum_both > 100:
        items['MedKit'] += 1
        new_med = medicaments.pop()
        new_med += (sum_both - 100)
        medicaments.append(new_med)
    elif sum_both == 100:
        items['MedKit'] += 1
    elif sum_both == 40:
        items['Bandage'] += 1
    elif sum_both == 30:
        items['Patch'] += 1
    else:
        pill += 10
        medicaments.append(pill)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

sorted_items = sorted(items.items(), key=lambda x: (-x[1], x[0]))
for item in sorted_items:
    if int(item[1]) > 0:
        print(f"{item[0]} - {item[1]}")

if medicaments:
    medicaments = sorted(list(map(str, medicaments)), reverse=True)
    print(f"Medicaments left: {', '.join(medicaments)}")

if textiles:
    textiles = list(map(str, textiles))
    print(f"Textiles left: {', '.join(textiles)}")
