def concatenate(*args, **kwargs):
    result = ''.join(args)
    for k, v in kwargs.items():
        if k in result:
            result = result.replace(k, v)
    return result
