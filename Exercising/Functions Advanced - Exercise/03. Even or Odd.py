def even_odd(*numbers):
    even_numbers = []
    odd_numbers = []
    if numbers[-1] == 'even':
        for number in numbers[:-1]:
            if number % 2 == 0:
                even_numbers.append(number)
        return even_numbers
    elif numbers[-1] == 'odd':
        for number in numbers[:-1]:
            if number % 2 != 0:
                odd_numbers.append(number)
        return odd_numbers
