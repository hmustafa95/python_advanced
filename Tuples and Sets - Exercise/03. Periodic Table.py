number = int(input())
chemicals = set()

for index in range(number):
    compound = input().split()
    for i in compound:
        chemicals.add(i)

for x in chemicals:
    print(x)