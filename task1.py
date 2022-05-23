class Error(Exception):
    """Base class for other Exc"""
    pass


class FormulaError(Error):
    """Input does not have 3 elements"""
    pass


def except_e(n: str):
    list_action = ['+', '-', '/', '*']
    if n not in list_action:
        raise FormulaError('Input does have 3 elements, second element must be +,-,/,*')


def calculate(solv: str):
    while True:
        try:
            valid_solv = [i for i in solv.split()]
            equal = (str(float(valid_solv[0]))) + valid_solv[1] + (str(float(valid_solv[-1])))
            if len(valid_solv) != 3:
                raise FormulaError('Input does have 3 elements, second element must be +,-,/,*')
            if except_e(valid_solv[1]):
                raise ValueError
            else:
                return eval(equal)

        except ValueError:
            print("ValueError")
            break
        except IndexError:
            print('You did not input anything')
            break


# print(calculate('2 a 2'))
print(calculate('2 + 2'))
# print(calculate('2 + 2'))
# print(calculate('a + 2'))

