from collections import deque

mils_caffeine = list(map(int, input().split(', ')))
energy_drinks = deque(map(int, input().split(', ')))
stamats_caffeine = 0

while mils_caffeine and energy_drinks:
    caffeine = mils_caffeine.pop()
    drink = energy_drinks.popleft()
    result = caffeine * drink
    if result + stamats_caffeine <= 300:
        stamats_caffeine += result
    else:
        energy_drinks.append(drink)
        stamats_caffeine -= 30
        if stamats_caffeine < 0:
            stamats_caffeine = 0

if energy_drinks:
    print(f"Drinks left: {', '.join(map(str, energy_drinks))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {stamats_caffeine} mg caffeine.")