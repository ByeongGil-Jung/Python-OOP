# 매직 메소드

"""
매직 메소드 (Magic Method)
-> __init__ 과 같이 오브젝트 안에서 실행되는 기본 클래스 메소드
-> 효율적인 코딩을 위해선 꼭 알아둬야 함!
"""


class Dog(object):
    def __init__(self, name, age):
        print('Name : {}, Age : {}'.format(name, age))


"""
일반적으로 사용하는 a + b 와 같은 오퍼레이터도
사실 내부적으로 a.__add__(b) 라는 매직 메소드가 동작하는 것이다.
"""


class MyInt(int):
    pass


class MyInt2(int):
    # __add__ 변경 (int 에서 string) 으로
    def __add__(self, other):
        return '{} plus {} is {}'.format(int(self), int(other), int(self) + int(other))


"""
즉, 클래스의 매직 메소드를 잘 오버라이딩 하면
정말 효율적이고 편리한 객체지향을 만들 수 있다.
"""


class Food(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return 'Item : {}, Price : {}'.format(self.name, self.price)


"""
lt (less than) :: <
등의 오퍼레이터의 return 값도 수정할 수 있다.
"""


class Food2(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __lt__(self, other):
        if self.price < other.price:
            return True
        else:
            return False

    def __add__(self, other):
        return self.price + other.price
