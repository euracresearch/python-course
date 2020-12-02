from basic.solutions.bot.farm import Farm

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
