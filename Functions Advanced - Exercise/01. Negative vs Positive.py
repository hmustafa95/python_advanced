list_numbers = [int(x) for x in input().split()]

def summary(numbers):
    positive = []
    negative = []
    for number in numbers:
        if number > 0:
            positive.append(number)
        elif number < 0:
            negative.append(number)
    total_positive = sum(positive)
    total_negative = sum(negative)
    print(total_negative)
    print(total_positive)
    if abs(total_negative) > abs(total_positive):
        return "The negatives are stronger than the positives"
    else:
        return "The positives are stronger than the negatives"

print(summary(list_numbers))