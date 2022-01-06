from collections import Counter


def can_be_poly(some_string: str) -> bool:
    if len(list(filter(lambda x: x % 2 != 0, Counter(some_string).values()))) <= 2:
        return True
    return False


print(can_be_poly('ababc'))
print(can_be_poly('abbbc'))
