from enum import IntEnum

class Types(IntEnum):
    FIRE = 0
    WATER = 1
    GRASS = 2
    NORMAL = 3
    ELECTRIC = 4

class Pokemon:
    _name = ''
    _main_type = Types.NORMAL

    def __init__(self, level, hp, attack, defense):
        self._defense = defense
        self._hp = hp
        self._attack_power = attack
        self._level = level

    def attack(self, enemy):
        print(self._name, 'attacks with a', self._attack_power, 'power', self._main_type.name, 'move!')
        enemy.take_damage(self._attack_power, self._main_type)

    def take_damage(self, power, attack_type):
        damage = power-self._defense
        self._hp -= damage
        self._print_damage(damage)

    def _print_damage(self, damage):
        print(self._name, 'took', damage, 'damage!')
        print(self._name, 'now has', self._hp, 'hp left.')

    @classmethod
    def get_name(cls):
        return cls._name


class Squirtle(Pokemon):
    _name = 'Squirtle'
    _main_type = Types.WATER

    def __init__(self, level, hp, attack, defense):
        super().__init__(level, hp, attack, defense)

    def take_damage(self, power, attack_type):
        damage = power-self._defense
        if attack_type == Types.WATER or attack_type == Types.FIRE:
            damage *= 0.5
        elif attack_type == Types.GRASS or attack_type == Types.ELECTRIC:
            damage *= 2
        damage = int(damage)
        self._hp -= damage
        self._print_damage(damage)


class Charmander(Pokemon):
    _name = 'Charmander'
    _main_type = Types.FIRE

    def __init__(self, level, hp, attack, defense):
        super().__init__(level, hp, attack, defense)

    def take_damage(self, power, attack_type):
        damage = power-self._defense
        if attack_type == Types.WATER:
            damage *= 2
        elif attack_type == Types.GRASS or attack_type == Types.FIRE:
            damage *= 0.5
        damage = int(damage)
        self._hp -= damage
        self._print_damage(damage)


class Bulbasaur(Pokemon):
    _name = 'Bulbasaur'
    _main_type = Types.GRASS

    def __init__(self, level, hp, attack, defense):
        super().__init__(level, hp, attack, defense)
    
    def take_damage(self, power, attack_type):
        damage = power - self._defense
        if attack_type == Types.FIRE:
            damage *= 2
        elif attack_type == Types.ELECTRIC or attack_type == Types.GRASS or attack_type == Types.WATER:
            damage *= 0.5
        damage = int(damage)
        self._hp -= damage
        self._print_damage(damage)


class Pikachu(Pokemon):
    _name = 'Pikachu'
    _main_type = Types.ELECTRIC

    def __init__(self, level, hp, attack, defense):
        super().__init__(level, hp, attack, defense)

    def take_damage(self, power, attack_type):
        damage = power - self._defense
        if attack_type == Types.ELECTRIC:
            damage *= 0.5
        damage = int(damage)
        self._hp -= damage
        self._print_damage(damage)


def start_battle(pokemon_a, pokemon_b):
    pokemon_a.attack(pokemon_b)
    pokemon_b.attack(pokemon_a)


def read_pokemon_data():
    return map(int, input().split())


def check_pkmn(_nome, level, hp, attack, defense):
    if(_nome.lower() == 'bulbasaur'):
        pkmn = Bulbasaur(level, hp, attack, defense)
    elif(_nome.lower() == 'charmander'):
        pkmn = Charmander(level, hp, attack, defense)
    elif(_nome.lower() == 'pikachu'):
        pkmn = Pikachu(level, hp, attack, defense)
    else:
        pkmn = Squirtle(level, hp, attack, defense)
    return pkmn


def main():
    pokemons = []
    for i in range(0, 2):
        nome = input()
        level, hp, attack, defense = read_pokemon_data()
        pokemons.append(check_pkmn(nome, level, hp, attack, defense))
    start_battle(pokemons[0], pokemons[1])

if __name__ == '__main__':
    main()
