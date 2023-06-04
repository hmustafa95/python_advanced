def operate(operator, *numbers):
    result = 0
    if operator == '+':
        for number in numbers:
            result += number
        return result
    elif operator == '-':
        for number in numbers:
            result -= number
        return result
    elif operator == '*':
        result = 1
        for number in numbers:
            result *= number
        return result
    elif operator == '/':
        result = numbers[0]
        for number in numbers:
            result /= number
        return result
