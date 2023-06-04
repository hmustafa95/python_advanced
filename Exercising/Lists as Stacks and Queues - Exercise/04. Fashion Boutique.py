clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
racks = 1
temp = 0

for index in range(len(clothes)):
    if temp + clothes[-1] > rack_capacity:
        racks += 1
        clothes.pop()
    elif temp + clothes[-1] == rack_capacity:
        temp = 0
        clothes.pop()
        if clothes:
            racks += 1
    else:
        temp += clothes.pop()

print(racks)