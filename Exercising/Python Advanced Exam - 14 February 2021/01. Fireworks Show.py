from collections import deque

effects = deque(map(int, input().split(', ')))
explosive_power = list(map(int, input().split(', ')))
crossette = 0
willow = 0
palm = 0

while effects and explosive_power:
    if crossette == 3 and willow == 3 and palm == 3:
        break
    effect = effects.popleft()
    if effect <= 0:
        continue
    power = explosive_power.pop()
    if power <= 0:
        effects.insert(0, effect)
        continue
    result = effect + power
    if result % 3 == 0 and result % 5 != 0:
        palm += 1
    elif result % 5 == 0 and result % 3 != 0:
        willow += 1
    elif result % 3 == 0 and result % 5 == 0:
        crossette += 1
    else:
        effect = effect - 1
        effects.append(effect)
        explosive_power.append(power)

if crossette >= 3 and willow >= 3 and palm >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if effects:
    print(f"Firework Effects left: {', '.join(map(str, effects))}")

if explosive_power:
    print(f"Explosive Power left: {', '.join(map(str, explosive_power))}")

print(f"Palm Fireworks: {palm}\nWillow Fireworks: {willow}\nCrossette Fireworks: {crossette}")