class ReverseIter:
    def __init__(self, list_revers: list):
        self.list_revers = list_revers

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.list_revers):
            self.n -= 1
            try:
                result = self.list_revers[self.n]
                return result
            except IndexError:
                print('Iteration out of range')
        else:
            raise StopIteration


a = ReverseIter([1, 2, 3, 4, 5])
a.__iter__()
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())

