def symmetric_difference():
    # Time for coding!
    # How would you obtain the symmetric difference of two sets by using the for cycle?
    fruits = {'apple', 'banana', 'kiwi', 'mango', 'peach', 'avocado', 'tomato'}
    vegetables = {'celery', 'tomato', 'potato', 'eggplant', 'lettuce', 'avocado'}

    # Method 1
    new_set = set()
    for fruit_item in fruits:
        if fruit_item not in vegetables:
            new_set.add(fruit_item)

    for vegetable_item in vegetables:
        if vegetable_item not in fruits:
            new_set.add(vegetable_item)

    # Method 2
    print((fruits ^ vegetables) - (fruits & vegetables))

    # Method 3
    print(fruits.symmetric_difference(vegetables))


def manual_zip():
    keys = ['title', 'author', 'year', 'pages']
    values = ['Resto qui', 'Marco Balzano', 2018, 168]

    # Method 1
    book = {}
    for index, key in enumerate(keys):
        book[key] = values[index]

    # Method 2
    book = {}

    index = 0
    while index < len(keys):
        book[keys[index]] = values[index]
        index += 1

    # Method 3 (list comprehension)
    book = {
        key: values[index]
        for index, key in enumerate(keys)
    }


def agent_fruits():
    agents = {
        'agent_007': {
            'first_name': 'James',
            'last_name': 'Bond',
            'married': False,
            'age': 40,
            'favorite_number': 3.1416,
            'phone': '1-800-007007',
            'weekly_fruits': ['avocado', 'apple', 'pear', 'tomato', 'avocado', 'tomato', 'watermelon']
        },
        'agent_004': {
            'first_name': 'Frederick',
            'last_name': 'Warder',
            'married': True,
            'age': 25,
            'favorite_number': 4,
            'phone': '1-800-004004',
            'weekly_fruits': ['mango', 'mango', 'peach', 'grape']
        },
        'agent_006': {
            'first_name': 'Alec',
            'last_name': 'Trevelyan',
            'married': False,
            'age': 35,
            'favorite_number': 0,
            'phone': '1-800-006006',
            'weekly_fruits': ['watermelon', 'grape', 'avocado']
        }
    }

    # Method 1
    fruits_counter = {}
    for agent_name, agent_info in agents.items():
        for fruit in agent_info['weekly_fruits']:
            if fruit not in fruits_counter:
                fruits_counter[fruit] = 1
            else:
                fruits_counter[fruit] += 1

    # Method 2
    fruits_counter = {}
    for agent_name, agent_info in agents.items():
        for fruit in agent_info['weekly_fruits']:
            fruits_counter[fruit] = fruits_counter.get(fruit, 0) + 1

    print(fruits_counter)
