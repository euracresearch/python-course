def pythagorean_theorem():
    import math
    a = 1
    b = 2

    # Method 2
    c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))

    # Method 2
    # math.sqrt(a ** 2 + b ** 2)


def string_reverse():
    string_variable = 'hello world'
    reversed_string = string_variable[::-1]


def string_concatenation():
    telephone = '0123-5678'
    telephone[:4] + '4' + telephone[5:]


def string_format():
    integer = -12345
    integer_2 = -8888
    double = 3.141592653589793
    word = 'python'

    string_1 = "Still missing: {amount} €"

    string_1.format(amount=integer)
    string_1.format(amount=integer_2)
    f"the pigreco value is around: {double:.5f}"

    f"   {word}   "
    "   %s   " % (word,)


def lists_kiwi_banana():
    # fruits = ['banana', 'apple', 'apricot', 'kiwi', 'grape', 'pineapple']
    fruits = ['avocado', 'apricot', 'kiwi', 'banana', 'pineapple', 'melon']
    # fruits = ['kiwi', 'apple', 'grape', 'apricot', 'watermelon', 'banana']

    # Remove before checking index of banana, otherwise 'banana'
    # can give you a wrong index if it is after
    fruits.remove('kiwi')

    banana_index = fruits.index('banana')
    fruits.insert(banana_index, 'kiwi')

    fruits


