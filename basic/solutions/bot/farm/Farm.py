from ..animals import *
from ..animals.Abstracts import PetAnimal, FarmAnimal


# --------------
# Farm behaviour
# --------------


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
