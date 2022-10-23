def func_executor(*args):
    result = ''
    for idx in args:
        result += f"{idx[0].__name__} - {idx[0](*idx[1])}" + '\n'
    return result

def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))