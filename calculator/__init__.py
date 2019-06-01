from calculator.model import Calculator
if __name__ == '__main__':

    calc = Calculator(int(input('첫번째 수')),int(input('두번째 수')))
    print('{} + {} = {}'.format(calc.first, calc.second, calc.sum()))
