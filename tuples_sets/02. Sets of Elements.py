first = set()
second = set()

number = input().split()
numarized = [int(x) for x in number]
number_one = numarized[0]
number_two = numarized[1]

for index in range(sum(numarized)):
    input_number = int(input())
    if index < number_one:
        first.add(input_number)
    else:
        second.add(input_number)

unique_set = set()

for first_index in first:
    for second_index in second:
        if first_index == second_index:
            unique_set.add(first_index)

for i in unique_set:
    print(i)