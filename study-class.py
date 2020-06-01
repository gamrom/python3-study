class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, power):
        print(f"{power}만큼 공격을 합니다")

class DefenceUnit(Unit):
    def __init__(self, name, hp, guard):
        Unit.__init__(self, name, hp)
        self.guard = guard

    def defence(self, power):
        print(f"{power}만큼 방어를 합니다")


class SpecialUnit(AttackUnit, DefenceUnit):
    def __init__(self, name, hp, damage, guard):
        AttackUnit.__init__(self, name, hp, damage)
        DefenceUnit.__init__(self, name, hp, guard)

unit1 = SpecialUnit("스페셜유닛", 100, 30, 20)
