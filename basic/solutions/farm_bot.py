"""
farm/
    __init__.py
    Farm.py
animals
    __init__.py
    Abstracts.py
    Pets.py
    Farm.py
farm_bot.py
"""

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


# -----------
# Pet animals
# -----------
# from .Abstracts import PetAnimal
class Dog(PetAnimal):
    icon = '🐶'

    def __init__(self, name: str):
        PetAnimal.__init__(self, name=name)
        self.tricks = 0

    def eat(self, food):
        super().eat(food)

        # Dogs are special, if they eat cookies they will do more tricks
        if food == 'cookies':
            self.tricks += 1


class Cat(PetAnimal):
    icon = '🐱'


# ------------
# Farm animals
# ------------
# from .Abstracts import FarmAnimal

class Cow(FarmAnimal):
    icon = "🐮"
    produce_value = '🥛'


class Chicken(FarmAnimal):
    icon = "🐔"
    produce_value = '🥚'


"""
# __init__.py
from .Farm import Cow, Chicken
from .Pets import Dog, Cat

__all__ = (
    'Cow',
    'Chicken',
    'Dog',
    'Cat'
)
"""


# --------------
# Farm behaviour
# --------------
# from animals import *
# from animals.Abstracts import PetAnimal, FarmAnimal


class Farm:
    def __init__(self):
        # List of animals in farm
        self.animals = {}

    def buy_animal(self, animal_type: str, *args):
        """
        Buy a type of animal

        :param animal_type: Type of animal to buy (dog, cat, chicken or cow)
        :param args: Arguments to pass to animal constructor
        :return:
        """
        # List of animals and classes
        animal_list = {
            'dog': Dog,
            'cat': Cat,
            'chicken': Chicken,
            'cow': Cow
        }

        if animal_type in self.animals:
            print(f'You already have {self.animals[animal_type]}')

        elif animal_type in animal_list:
            # Create new animal from list of animals
            animal = animal_list[animal_type](*args)

            # Store animal in list of animals in farm
            self.animals[animal_type] = animal
        else:
            print(f'Animal "{animal_type}" does not exist')

    def feed_animal(self, animal_type: str, food: str):
        """
        Feed an animal on farm

        :param animal_type: Type of animal name to feed
        :param food: Food to feed the animal with
        :return:
        """
        if animal_type in self.animals:
            # Call to method 'eat' from instance in list
            self.animals[animal_type].eat(food)
        else:
            print(f'Animal "{animal_type}" does not exist')

    def play_animal(self, animal_type: str):
        """
        Play with animal, the animal will do tricks

        :param animal_type: Animal type to play with
        :return:
        """
        if animal_type in self.animals:
            # Check if it a PetAnimal type with isinstance
            if isinstance(self.animals[animal_type], PetAnimal):
                # Do tricks for selected animal
                self.animals[animal_type].do_tricks()
            else:
                print(f'You cannot play with {self.animals[animal_type]}')
        else:
            print(f'Animal "{animal_type}" does not exist')

    def produce_animal(self, animal_type: str):
        """
        Animal will produce

        :param animal_type: Animal type to make it produce
        :return:
        """
        if animal_type in self.animals:
            if isinstance(self.animals[animal_type], FarmAnimal):
                self.animals[animal_type].produce()
            else:
                print(f'You cannot make {self.animals[animal_type]} to produce')
        else:
            print(f'Animal "{animal_type}" does not exist')


"""
# __init__.py
from .Farm import Farm

__all__ = (
    'Farm',
)
"""

# farm_bot.py
# from farm import Farm

if __name__ == '__main__':
    # -----------------
    # Start farm object
    # -----------------
    farm = Farm()

    # Print instructions
    print("""Welcome to the Farm bot!
You can make the following actions:
    
- Buy pet animal                buy [animal] [name]
- Buy farm animal               buy [animal] [name] [production unit]
- Feed animal                   feed [animal] [food]
- Play with animal              play [animal]
- Make an animal to produce     produce [animal]
- Sell all animals              sell
- Quit                          quit

[animal] can be 'cow', 'chicken', 'dog' or 'cat'

- You can play only with 'dog' and 'cat'
- You can make 'cow' and 'chicken' to produce
- If you feed your 'dog' with 'cookies', it will make more tricks

""")

    while True:
        # Wait for a command
        command = input('Select your command: ').split()

        command_length = len(command)
        if command_length == 0:
            continue

        action = command[0]

        if action == 'quit':
            break
        elif action == 'sell':
            # Initialize farm
            farm = Farm()
            print('No animals in your farm')
        else:
            # List with minimum of parameters to accept
            minimum_params = {
                'buy': 3,
                'feed': 3,
                'play': 2,
                'produce': 2
            }

            # Function to run based on first command
            options = {
                'buy': farm.buy_animal,  # 3/4 parameters
                'feed': farm.feed_animal,  # 3 parameters
                'play': farm.play_animal,  # 2 parameters
                'produce': farm.produce_animal  # 2 parameters
            }

            try:
                if command_length >= minimum_params[action]:
                    function = options[action]

                    # Pass all parameters in order
                    function(*command[1:])
                else:
                    print(f'Missing parameters for action "{action}"')
            except KeyError:
                pass
