class ValueCannotBeNegative(Exception):
    """Raised when a negative value occurs"""

for idx in range(5):
    number = int(input())
    if number < 0:
        raise ValueCannotBeNegative
