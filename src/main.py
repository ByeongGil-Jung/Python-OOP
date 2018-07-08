# Main Function
from src.exercise_1 import C_Employee as E, C_Student as S, C_Person as P
from src.exercise_2 import C_Unit as U
from src.exercise_3 import C_MagicMethod as M


def oopFirst():
    print('< Student >')
    s = S.Student('abc', 2, 3, 14)
    print(s.introduce_id())

    print()
    print('< Emplyee >')
    print('The number of employee :', E.Employee.num_of_emps)
    e1 = E.Employee('Hong', 'GilDong', 30000)
    e2 = E.Employee('Ga', 'NaDa', 50000)
    print(' - Adding employee e1, e2 ...')
    print('The number of employee :', E.Employee.num_of_emps)

    print('The full name of e1 :', e1.full_name())
    print('The full name of e2 :', e2.full_name())

    print()
    print('The of pay of e1 :', e1.pay)
    print('The of pay of e2 :', e2.pay)

    e1.apply_raise()
    e2.apply_raise()
    print(' - Increase the rate of increase ...')

    print('The of pay of e1 :', e1.pay)
    print('The of pay of e2 :', e2.pay)

    print()
    print('The number of employee :', E.Employee.num_of_emps)
    del e1
    print(' - Delete one employee ...')
    print('The number of employee :', E.Employee.num_of_emps)
    del e2
    print(' - Delete one employee ...')
    print('The number of employee :', E.Employee.num_of_emps)

    # print(e1.__dict__)
    # print(C_Employee.__dict__)
    # print('ㅋㄷㅋㄷ')
    # print(C_Employee.Employee.__dict__)

    print()

    """
    클래스 메소드
    """
    print('[ The part of \'Class Method\' ]')
    emp_1 = E.Employee('Sanghee', 'Lee', 50000)
    emp_2 = E.Employee('Minjung', 'Kim', 60000)

    print(emp_1.getPay())
    print(emp_2.getPay())

    """
    get_amount = input('연봉 인상률 : \n => ')
    get_amount = float(get_amount)
    """
    get_amount = 1.1
    E.Employee.change_raise_amount(get_amount)

    emp_1.apply_raise()
    emp_2.apply_raise()

    print(emp_1.getPay())
    print(emp_2.getPay())

    print()

    """
    일반 함수에서 def 로 정의한 함수를
    클래스 메소드로 바꾸기 (더 세련된 코드)
    """

    ssn_1 = '900829-1034356'
    ssn_2 = '051224-4061569'

    ssn_1_p = P.ssnParser(ssn_1)
    ssn_2_p = P.ssnParser(ssn_2)

    person_1 = P.Person(*ssn_1_p)
    person_2 = P.Person(*ssn_2_p)

    print(person_1)
    print(person_2)

    print()

    c_person_1 = P.Person.ssnConstructor(ssn_1)
    c_person_2 = P.Person.ssnConstructor(ssn_2)

    print(c_person_1)
    print(c_person_2)

    print()

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

    import datetime
    my_date = datetime.date(2016, 10, 9)

    # 클래스를 통해 스태틱 메소드 호출
    print(P.Person.isWorkDay(my_date))

    # 인스턴스를 통해 스태틱 메소드 호출
    print(person_1.isWorkDay(my_date))

    # -> 즉, 클래스와 인스턴스 모두 static method 에 접근 할 수 있다 !!


def superAndsubClass():
    goblin_1 = U.Goblin('Solider', 'small', 100, None, None)
    goblin_1.show_status()

    print('\n [ Let\'s see how to inherit it ]\n')
    print(U.Goblin.__dict__)
    # 여기선 show_status 가 없다.

    help(U.Goblin)
    """
    여기서 Goblin 클래스가 이름을 찾는 순서를 알 수 있다.
    자신의 네임 스페이스 -> 부모의 네임 스페이스 -> 최상위 오브젝트의 네임 스페이스
    
    즉, 인스턴스 생성시에 무조건 호출되어야 하는 init() 메소드를
    자신의 네임 스페이스에서 찾지 못 하면 부모 클래스에서 참조하게 된다.
    
    --> 여기선, 자신의 네임 스페이스에서 갖지 못했기에,
        부모 클래스의 init() 과 show_status() 를 가져왔다.
    """

    print()
    print(dir(U.Goblin))
    # 여기서 show_status 를 상속 받았음을 알 수 있다.
    print()

    # super() 와 오버라이드를 이용한 코딩
    goblin_2 = U.Goblin('Solider', 'Small', 100, 'Melee Attack', None)
    goblin_2.show_status()
    print()

    # 두번 상속
    sphere_goblin_1 = U.SphereGoblin('Solider', 'Small', 100, 'Range Attack', 10, 'Long Sphere')
    sphere_goblin_1.show_status()
    print()

    # 히어로 클래스 생성
    hero_1 = U.Hero('Hero', 'Big', 300, [goblin_1, goblin_2, sphere_goblin_1])
    hero_1.showOwnGoblins()
    hero_1.makeGoblinsAttack()
    print()

    # 고블린 추가 및 제거
    a_goblin_1 = U.Goblin('Solider', 'Small', 100, 'Melee Attack', 20)
    a_sphereGoblin_2 = U.SphereGoblin('Solider', 'Small', 100, 'Range Attack', 5, 'Long Sphere')

    hero_1.addGoblins([a_goblin_1, a_sphereGoblin_2])

    print('[ Before adding new goblin ]')
    hero_1.showOwnGoblins()
    hero_1.makeGoblinsAttack()

    hero_1.removeGoblin([a_goblin_1, a_sphereGoblin_2])

    print('\n[ Before deleting new goblin ]')
    hero_1.showOwnGoblins()
    hero_1.makeGoblinsAttack()
    print()

    # 만약 소유하고 있는(있지 않은) 고블린이라면?
    a_goblin_2 = U.Goblin('Solider', 'Small', 100, 'Melee Attack', 20)

    hero_1.addGoblins([goblin_1])
    hero_1.removeGoblin([a_goblin_2])


def magicMethod():
    # 자동으로 실행되는 __init__ 메소드
    dog_1 = M.Dog('Pink', '12')
    print()

    # int 를 상속받는 MyInt 생성
    my_num = M.MyInt(5)
    print(type(my_num))
    print(isinstance(my_num, int))
    # True 가 반환. MyInt 클래스가 int 타입인 것을 알 수 있음
    print(M.MyInt.__bases__)  # __bassess__ 는 클래스의 베이스 클래스를 알 수 있다.
    print()

    # 그렇담 MyInt 클래스와 int 의 덧셈은 가능할까?
    my_num_2 = M.MyInt(5)
    print(my_num_2 + 5)
    print(dir(my_num_2))  # 실제로 int 에 해당하는 매직 메소드들을 갖고 있음
    print()
    print(my_num_2.__add__(5))  # 여기서 int 의 매직메소드를 활용할 수 있음을 알 수 있다.
    print()

    # 이제 아예 MyNum 클래스의 __add__ 를 string return 으로 바꿔보자
    my_num2_1 = M.MyInt2(5)
    print(my_num2_1 + 5)  # string 이 반환된다.
    print()

    """
    built-in type 인 int, str, list, dict 등은 사용자들의 편리함을 위해
    자신의 타입에 맞게 각종 오퍼레이터를 오버로딩하는
    매직 메소드를 포함하고 있다.
    """
    print([1, 2, 3] + [4, 5, 6])
    print([1, 2, 3].__add__([4, 5, 6]))  # 매직 메소드

    print(len({'one': 1, 'tow': 2, 'three': 3}))
    print({'one': 1, 'two': 2, 'three': 3}.__len__())  # 매직 메소드
    print()

    # 인스턴스 자체의 정보를 출력하기 위해선 __str__ 메소드를 수정한다.
    food_1 = M.Food('Ice cream', 3000)
    print(food_1)  # 인스턴스 그 자체의 값을 다른 값으로 출력하였다.

    # lt (less than) 등의 오퍼레이터도 수정할 수 있다.
    food_2 = M.Food('Hamburger', 5000)
    # print(food_1 < food_2)
    # 당연히 에러남. Food 클래스의 비교를 어떻게 할 지 정의를 안했기 때문 !!
    # 엄밀히 얘기하면 주소값을 비교하기 때문에 애초에 비교가 성립되지 않음.
    print()

    """ __lt__ 를 수정한 후 """
    food2_1 = M.Food2('Ice cream', 3000)
    food2_2 = M.Food2('Hamburger', 5000)
    food2_3 = M.Food2('Cola', 2000)

    print(food2_1 < food2_2)
    print(food2_2 < food2_3)
    print(food2_1 < food2_3)
    print()

    # 추가로 __add__ 역시 적용해보자
    # print(food2_1.__add__(food2_2))
    # 위와 마찬가지로 클래스 끼리 add 하기 때문에 (엄밀히 말하면 주소값을 add)
    # 에러가 발생한다.
    # __add__ 메소드를 재정의 해서 다시 return 값을 바꿔줘야 한다.
    print(food2_1 + food2_2)


def main():
    print("\n========================================= [Exercise :: 1] =========================================\n")
    oopFirst()
    print("\n========================================= [Exercise :: 2] =========================================\n")
    superAndsubClass()
    print("\n========================================= [Exercise :: 3] =========================================\n")
    magicMethod()


if __name__ == '__main__':
    main()
