import pymongo

client = pymongo.MongoClient()
db = client['starwars_db']

characters = db.characters_col.find()
print(type(characters))

Luke = db.characters_col.find_one({"name": "Luke Skywalker"},
                                  {'films': 0, "species": 0, "homeworld": 0, "_id": 0})
print(Luke['name'])

# Q1: Darth Vader's name and height
print('\n')
print('Q1')
print('\n')
Darth_Vader = db.characters_col.find_one({"name": "Darth Vader"},
                                         {'name': 1, 'height': 1, '_id': 0})
print(Darth_Vader)

# Q2: Characters with yellow eyes, returning just their names
print('\n')
print('Q2')
print('\n')
yellow_eyes = db.characters_col.find({'eye_color': 'yellow'},
                                     {'name': 1, '_id': 0})
for person in yellow_eyes:
    print(person)

# Q3: Find all male characters. show first 3
print('\n')
print('Q3')
print('\n')
male = db.characters_col.find({'gender': 'male'},
                              {'name': 1, '_id': 0}).limit(3)
for man in male:
    print(man)

# Q4: Find all humans whose home planet is Alderaan
print('\n')
print('Q4')
print('\n')
human_Alderaan = db.characters_col.find({'species.name': 'Human', 'homeworld.name': 'Alderaan'},
                                        {'name': 1, '_id': 0})
for pers in human_Alderaan:
    print(pers)

#Have some fun playing with aggregates
print('\n')
print('Playing with aggregates')
print('\n')

pipeline = [
    {
        "$group": {"_id": "$homeworld.name",
        'avg_height': {'$avg': '$height'}}
    }
]
avg_height = db.characters_col.aggregate(pipeline)
for h in avg_height:
    print(h)
