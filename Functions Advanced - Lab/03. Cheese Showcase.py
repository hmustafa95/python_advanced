def sorting_cheeses(**kwargs):
    kwargs = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = []
    for (cheese, quantity) in kwargs:
        result.append(cheese)
        quantity_list = sorted(quantity, reverse=True)
        result += quantity_list
    return '\n'.join([str(x) for x in result])
