# super class 인 Unit
class Unit(object):
    def __init__(self, rank, size, life):
        self.name = self.__class__.__name__
        self.rank = rank
        self.size = size
        self.life = life

    def __str__(self):
        return 'Name : {}'.format(self.name)

    def show_status(self):
        print('Name : {}'.format(self.name))
        print('Grade : {}'.format(self.rank))
        print('Size : {}'.format(self.size))
        print('Life : {}'.format(self.life))


# sub class 인 Goblin
class Goblin(Unit):
    # pass -> ?? 패스가 뭐야 (단순히 실행할 코드가 없다는 것을 의미)
    """
    Unit(super class) 의 하위인 Goblin(sub class) 는
    어떠한 메소드나 속성을 정의하지 않았는데도
    
    Unit 클래스 안에 정의한 show_status 메소드를 상속받아 사용할 수 있다.
    """

    # 상위 클래스의 메소드를 자신의 클래스에서 재정의하는 오버라이드를 쓸 것임.

    def __init__(self, rank, size, life, attack_type, damage):
        super(Goblin, self).__init__(rank, size, life)
        self.attack_type = attack_type
        self.damage = damage
        """
        super class 에 접근하기 위해선,
        super(자식 클래스, self).메소드명()
        
        과 같이 접근한다.
        """

    def show_status(self):
        super(Goblin, self).show_status()
        print('Attack Type: {}'.format(self.attack_type))
        # 오버라이드 메소드
        print('Damage : {}'.format(self.damage))

    # 공격 메소드 추가
    def attack(self):
        print('[{}] attacks. // Damage :: ({})'.format(self.name, self.damage))


class SphereGoblin(Goblin):
    def __init__(self, rank, size, life, attack_type, damage, sphere_type):
        super(SphereGoblin, self).__init__(rank, size, life, attack_type, damage)
        self.sphere_type = sphere_type

    def show_status(self):
        super(SphereGoblin, self).show_status()
        print('Type of Sphere : {}'.format(self.sphere_type))


# 고블린을 거느리는 Hero 클래스
class Hero(Unit):
    def __init__(self, rank, size, life, goblins=None):
        super(Hero, self).__init__(rank, size, life)
        if goblins is None:
            self.goblins = []
        else:
            self.goblins = goblins
        """
        만약 고블린 리스트를 인자로 받을 경우(값이 있을 경우)
        self.goblins 에 그 값을 넣는다.
        """

    def showOwnGoblins(self):
        # isinstance() 를 사용해서 객체의 타입을 비교할 수 있다.
        # -> class 에 따라 bool 값 반환 가능
        num_of_goblins = len([x for x in self.goblins if isinstance(x, Goblin)])
        num_of_sphereGoblins = len([x for x in self.goblins if isinstance(x, SphereGoblin)])
        print(' - Currently, {} owns {} goblins, and owns {} sphere goblins'.format(self.name, num_of_goblins, num_of_sphereGoblins))

    def makeGoblinsAttack(self):
        for goblin in self.goblins:
            goblin.attack()

    # 고블린 추가 및 제거
    def addGoblins(self, new_goblins):
        for goblin in new_goblins:
            if goblin not in self.goblins:
                self.goblins.append(goblin)
            else:
                print(' - It is already added goblins.')

    def removeGoblin(self, old_goblins):
        for goblin in old_goblins:
            try:
                self.goblins.remove(goblin)
            except:
                print(' - You do NOT own {}'.format(goblin))
