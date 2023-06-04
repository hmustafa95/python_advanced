number = int(input())
chemicals = set()

for idx in range(number):
    compounds = input().split()
    for compound in compounds:
        chemicals.add(compound)

for chemical in chemicals:
    print(chemical)