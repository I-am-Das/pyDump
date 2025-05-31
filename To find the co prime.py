import math


def gcd(a, b):
    return math.gcd(a, b)


def are_three_numbers_mutually_coprime(numbers):
    if not isinstance(numbers, list) or len(numbers) != 3:
        return False
    a, b, c = numbers
    if gcd(a, b) == 1 and gcd(a, c) == 1 and gcd(b, c) == 1:
        return True
    else:
        return False


list1 = []
for i in range(3):
    d = int(input())
list1.append(d)
print(f"{list1} co-prime: {are_three_numbers_mutually_coprime(list1)}")
