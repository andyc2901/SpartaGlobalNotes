import json
import requests
import pandas as pd


# Find attribute functions take the request and pulls the desired attribute


def find_name(poke_req):
    name = poke_req.json()['name']
    return name


def find_id(poke_req):
    pokedex_num = poke_req.json()['id']
    return pokedex_num


def find_ability(poke_req):
    abilities = []
    for x in range(len(poke_req.json()['abilities'])):
        if not poke_req.json()['abilities'][x]['is_hidden']:
            abilities.append(poke_req.json()['abilities'][x]['ability']['name'])
    return abilities


def find_types(poke_req):
    try:
        type1 = poke_req.json()['types'][0]['type']['name']
        type2 = poke_req.json()['types'][1]['type']['name']
    except IndexError:
        type1 = poke_req.json()['types'][0]['type']['name']
        type2 = 'NA'
    return type1, type2


def find_weight(poke_req):
    weight = poke_req.json()['weight']
    return weight


def find_height(poke_req):
    height = poke_req.json()['height']
    return height


def find_stats(poke_req):
    hp = poke_req.json()['stats'][0]['base_stat']
    attack = poke_req.json()['stats'][1]['base_stat']
    defense = poke_req.json()['stats'][2]['base_stat']
    sp_attack = poke_req.json()['stats'][3]['base_stat']
    sp_defense = poke_req.json()['stats'][4]['base_stat']
    speed = poke_req.json()['stats'][5]['base_stat']
    stats = [hp, attack, defense, sp_attack, sp_defense, speed]
    return stats


# take all the attributes and create the dictionary for the pokedex entry


def setup_pokedex_entry(pokedex_id):
    pokedex_entry = {
        'name': find_name(pokedex_id),
        'id': find_id(pokedex_id),
        'type': find_types(pokedex_id),
        'abilities': find_ability(pokedex_id),
        'weight': find_weight(pokedex_id),
        'height': find_height(pokedex_id),
        'Base stats': {'hp': find_stats(pokedex_id)[0],
                       'attack': find_stats(pokedex_id)[1],
                       'defense': find_stats(pokedex_id)[2],
                       'special attack': find_stats(pokedex_id)[3],
                       'special defense': find_stats(pokedex_id)[4],
                       'speed': find_stats(pokedex_id)[0]
                       }
    }
    return pokedex_entry


# Pull the details for every pokemon in the original 151
poke_req_all = requests.get("https://pokeapi.co/api/v2/pokemon?limit=1010&offset=0")

poke_dex = poke_req_all.json()['results']
# Create the simplified pokedex entries in dictionary form
pokedex = []
for x in range(150):
    every_detail = requests.get(poke_dex[x]['url'])
    pokedex.append(setup_pokedex_entry(every_detail))

print(pokedex)

# Write the pokedex json format

with open('Pokedex151.json', 'w') as JsonOut:
    json.dump(pokedex, JsonOut)

pokedex1 = pd.read_json('Pokedex151.json')
pokedex1.to_csv("Pokedex151.csv", index=False)
