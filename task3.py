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


for i in fibonacci_list(11):
    print(i)