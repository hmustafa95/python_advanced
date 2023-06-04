elements = list(map(int, input().split()))
first_set = set()
second_set = set()

for idx in range(elements[0]):
    first_set.add(int(input()))

for _ in range(elements[1]):
    second_set.add(int(input()))

result = set()

for current_number in first_set:
    if current_number in second_set:
        result.add(current_number)

for number in result:
    print(number)