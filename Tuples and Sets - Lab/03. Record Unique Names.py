number = int(input())
list_of_names = []
unique_list = []

for index in range(number):
    name = input()
    list_of_names.append(name)

for x in list_of_names:
    if x not in unique_list:
        unique_list.append(x)

for y in unique_list:
    print(y)