def fibonacci_list(n: int) -> list:
    n1, n2 = 0, 1
    count = 0
    equal = []

    while count < n:
        for i in range(n):
            equal.append(n1)
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            count += 1
        yield equal


def fibon_list(n):
    """ Version with func"""
    for a in fibonacci_list(n):
        print(a)


fibon_list(11)
