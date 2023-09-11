import json
import random

with open('Pokedex151.json') as pokedex:
    all151 = json.load(pokedex)

poke_id = random.randint(0, 150)
poke_details = all151[poke_id]
name = poke_details['name']
# print(poke_details)
guess = ''
hint_counter = 0
game = True
details = {'base stats': poke_details['Base stats'],
           'weight': poke_details['weight'],
           'height': poke_details['height'],
           'abilities': poke_details['abilities'],
           'type': poke_details['type'],
           'ID': poke_details['id']}

print('Welcome to Who Is That Pokemon: 151 Edition!')
print('I will show you different stats about the pokemon and you can guess until you get it right or give up!')
print('To give up, simply type "give up"')
print('Here are the base stats of the pokemon: ')
print(details['base stats'])
while game:

    guess = input('Please enter your guess: ')
    if guess == name:
        print('YOU WIN!! The pokemon was', name)
        game = False

    elif guess == 'give up':
        print('You gave up! The pokemon was', name)
        game = False

    elif guess != name:
        print('Incorrect guess')
        hint = input('Please enter 1 if you would like a hint, or 0 to guess again ')

        try:
            if int(hint) == 1:
                hint_counter += 1
            elif int(hint) != 0 and int(hint) != 1:
                print('Please only input a 1 or a 0')
        except ValueError:
            print('Please only input a 1 or 0')

        if hint_counter == 1:
            print('Here is your next hint')
            print(details['base stats'])
            print('Weight: ', details['weight'])
            print('Height: ', details['height'])

        elif hint_counter == 2:
            print('Here is your next hint')
            print(details['base stats'])
            print('Weight: ', details['weight'])
            print('Height: ', details['height'])
            print('Abilities: ', details['abilities'])

        elif hint_counter == 3:
            print('Here is your next hint')
            print(details['base stats'])
            print('Weight: ', details['weight'])
            print('Height: ', details['height'])
            print('Abilities: ', details['abilities'])
            print('Type: ', details['type'])

        elif hint_counter == 4:
            print('Here is your next hint')
            print(details['base stats'])
            print('Weight: ', details['weight'])
            print('Height: ', details['height'])
            print('Abilities: ', details['abilities'])
            print('Type: ', details['type'])
            print('ID', details['ID'])

        elif hint_counter >= 5:
            print('You are out of hints')
            print(details['base stats'])
            print('Weight: ', details['weight'])
            print('Height: ', details['height'])
            print('Abilities: ', details['abilities'])
            print('Type: ', details['type'])
            print('ID', details['ID'])
