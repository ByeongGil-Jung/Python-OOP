class Person(object):
    def __init__(self, year, month, day, sex):
        self.year = year
        self.month = month
        self.day = day
        self.sex = sex

    def __str__(self):
        return 'The Birthday :: {} years, {} month, {} rd \nGender :: {}'.format(self.year, self.month, self.day, self.sex)

    @classmethod
    def ssnConstructor(cls, ssn):
        # ssn 은 주민등록번호
        (front, back) = ssn.split('-')
        sex = back[0]

        if sex == '1' or sex == '2':
            year = '19' + front[0:2]
        else:
            year = '20' + front[0:2]

        if int(sex) % 2 == 1:
            sex = 'Male'
        else:
            sex = 'Female'

        month = front[2:4]
        day = front[4:6]

        """
        여기서 cls 로 return 하는 것은
        클래스 생성자로 return 하는 것을 의미한다.
        
        즉 cls 는 class 자체를 의미한다고 볼 수 있다.
        """
        return cls(year, month, day, sex)

    """
    밑에는 static method 임
    
    - 클래스 메소드
     클래스 메소드는 클래스를 통하여 호출되고, 첫번재 인자로 클래스 자신이 전달된다.
    이 인자를 cls 라 칭한다.
    
    - 스태틱 메소드
     스태틱 메소드는 클래스 안에서 정의되어 클래스 네임 스페이스 안에 있을 뿐이다.
    즉, 실제로는 일반 함수와 전혀 다를게 없다.
    
    -> 하지만 클래스와 연관성이 있는 함수를 클래스 안에 정의하여,
    클래스나 인스턴스를 통해서 호출하여 조금 편하게 쓸 수 있다.
    
    (즉, 클래스 내에서
    클래스와 인스턴스 둘 다 접근 가능한 함수를 만들 때
    static method 를 만들어서 사용한다.)
    """

    @staticmethod
    def isWorkDay(day):
        # weekday() 함수의 리턴값은
        # 월: 0, 화: 1, 수: 2, 목: 3, 금: 4, 토: 5, 일: 6
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True


# 일반 함수
def ssnParser(ssn):
    # ssn 은 주민등록번호
    (front, back) = ssn.split('-')
    sex = back[0]

    if sex == '1' or sex == '2':
        year = '19' + front[0:2]
    else:
        year = '20' + front[0:2]

    if int(sex) % 2 == 1:
        sex = 'Male'
    else:
        sex = 'Female'

    month = front[2:4]
    day = front[4:6]

    return year, month, day, sex
