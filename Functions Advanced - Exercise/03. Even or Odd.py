def even_odd(*numbers):
    even_list = []
    odd_list = []
    if numbers[-1] == 'even':
        for number in numbers[:-1]:
            if number % 2 == 0:
                even_list.append(number)
        return even_list
    elif numbers[-1] == 'odd':
        for number in numbers[:-1]:
            if number % 2 != 0:
                odd_list.append(number)
        return odd_list
