# Python Dicts and JSONs are very similar, but need to be careful when comparing the two
# JSON is one long string, need to convert to a pythong Dict to use Dict methods

import json

course = {"name": "Data 249", "trainer": "Paula"}
print(course)
print(type(course))

# Writing JSON files
# two main json methods for writing, one writes to a string, one writes to a file (dumps,dump)

# '''
course_json_str = json.dumps(course)

print(course_json_str)
print(type(course_json_str))

with open("new_json_data.json",'w') as jsonfile:
    json.dump(course, jsonfile)
# '''

# Loading JSON
# two main json methods for reading, one reads a string, one reads a file (loads/load)

# '''
with open("new_json_data.json") as jsonfile:
    course_file = json.load(jsonfile)
    print(course_file['name'])
    print(type(course_file))
# '''

# '''
course_dict = json.loads(course_json_str)
print(course_dict)
# '''
