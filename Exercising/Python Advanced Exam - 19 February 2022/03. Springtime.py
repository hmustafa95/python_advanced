def start_spring(**kwargs):
    my_dict = {}
    result = ''
    for k, v in kwargs.items():
        if v not in my_dict:
            my_dict[v] = []
        my_dict[v].append(k)
    my_dict = dict(sorted(my_dict.items(), key=lambda x: (-len(x[1]), x[0])))
    for k, v in my_dict.items():
        my_dict[k].sort()
        result += f'{k}:' + '\n'
        for item in v:
            result += f'-{item}' + '\n'
    return result
