number_list = list(map(int, input().split()))
positive = []
negative = []

for idx in number_list:
    if idx > 0:
        positive.append(idx)
    else:
        negative.append(idx)

print(sum(negative))
print(sum(positive))

if abs(sum(negative)) > sum(positive):
    print('The negatives are stronger than the positives')
else:
    print('The positives are stronger than the negatives')