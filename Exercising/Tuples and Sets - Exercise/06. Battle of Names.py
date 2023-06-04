number = int(input())
names = []
even_set = set()
odd_set = set()

for _ in range(number):
    names.append(input())

value = 0
counter = 1
for name in names:
    for letter in name:
        value += ord(letter)
    value = value // counter
    if value % 2 != 0:
        odd_set.add(value)
    else:
        even_set.add(value)
    value = 0
    counter += 1

sum_even = sum(even_set)
sum_odd = sum(odd_set)

if sum_odd == sum_even:
    print(*set.union(odd_set, even_set), sep=', ')
elif sum_odd > sum_even:
    print(*set.difference(odd_set, even_set), sep=', ')
else:
    print(*set.symmetric_difference(odd_set, even_set), sep=', ')