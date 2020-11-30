from abc import ABC


# ----------------
# Abstract classes
# ----------------
class Animal(ABC):
    icon = None

    def __init__(self, name: str):
        self.name = name
        self.food = []

    def eat(self, food: str):
        """
        Feed animal with food

        :param food: Food to feed with
        :return:
        """
        print(f'{self.full_name} thank you for the {food}')
        self.food.append(food)

    @property
    def full_name(self):
        """
        Full name, composed by icon and name

        :return:
        """
        return f'[{self.icon} {self.name}]'

    def __str__(self):
        return f'{self.icon} {self.name}'


class PetAnimal(Animal):
    """
    Class to define animals that can do tricks
    """

    def __init__(self, name: str):
        Animal.__init__(self, name=name)

        # By default, the pet animal does 1 trick
        self.tricks = 1

    def do_tricks(self):
        print(f'{self.full_name} does {self.tricks} trick(s)')


class FarmAnimal(Animal):
    """
    Class to define animals that can produce
    """

    produce_value = ''

    def __init__(self, name: str, unit: int = 0):
        Animal.__init__(self, name=name)

        try:
            self.unit = int(unit)
        except ValueError:
            self.unit = 0

        self.__total_produced = 0

    def produce(self):
        if self.unit > 0:
            print(f'{self.full_name} produces {self.produce_value * self.unit}')

        self.__total_produced += self.unit
