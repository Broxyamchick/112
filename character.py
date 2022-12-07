class Is_alive:
    pass


class Character:
    name = ""
    hp = 100
    damage = 1
    defense = 0

    def __init__(self, name, hp=100, damage=1, defense=0):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.defense = defense

    def __str__(self):
        return f' == {self.name} ==\n' \
        f' Здоровье: {self.hp} \n' \
        f' Урон: {self.damage} \n' \
        f' Защита: {self.defense} \n'

    def take_damage(self, damage):
        self.hp -= damage

    def attack(self, target):
        target.take_damage(self.damage)

    def is_alive(self, hp):
        if hp== 0:
            Is_alive==("true")
        else:
            print("")
        




