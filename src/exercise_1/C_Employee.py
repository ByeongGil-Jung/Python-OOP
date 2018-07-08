class Employee(object):

    raise_amount = 1.1
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@naver.com'

        Employee.num_of_emps += 1

    def __del__(self):
        Employee.num_of_emps -= 1

    @classmethod
    def change_raise_amount(cls, amount):
        while amount < 1:
            print('[WARNING] The rate of increase can NOT be less than \'1\'.')
            amount = input('(Input) Please input again the increase rate \n => ')
            amount = float(amount)
        cls.raise_amount = amount
        print(' - The increase rate of {} was applied.'.format(amount))
    """
    즉, 클래스 메소드는 클래스 변수의 값을 변경할 떄 쓰이는 메소드이다.
    """

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    ####
    def getPay(self):
        return 'Currently, The salary of {} is {}'.format(self.full_name(), self.pay)
