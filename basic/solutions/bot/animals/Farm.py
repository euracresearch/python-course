from .Abstracts import FarmAnimal


# ------------
# Farm animals
# ------------


class Cow(FarmAnimal):
    icon = "🐮"
    produce_value = '🥛'


class Chicken(FarmAnimal):
    icon = "🐔"
    produce_value = '🥚'
