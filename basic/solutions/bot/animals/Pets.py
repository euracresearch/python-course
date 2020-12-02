from .Abstracts import PetAnimal


# -----------
# Pet animals
# -----------

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
