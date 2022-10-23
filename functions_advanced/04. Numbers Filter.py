def even_odd_filter(**kwargs):
    my_dict = {}
    for k, v in kwargs.items():
        if k == 'even':
            my_dict[k] = [x for x in v if x % 2 == 0]
        else:
            my_dict[k] = [x for x in v if x % 2 != 0]
    return dict(sorted(my_dict.items(), key=lambda x: len(x[1]), reverse=True))
