def kwargs_length(**dict):
    result = 0
    for k, v in dict.items():
        if k:
            result += 1
    return result
