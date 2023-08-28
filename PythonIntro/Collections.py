## Lists

#example_list = [1,True, "string"]


shopping_list = ['eggs','bread','cheese']
print(shopping_list)
print(type(shopping_list))

shopping_list[1] = "bananas"

shopping_list.append('bread')

shopping_list.pop(0)

shopping_list.index('bread')

print(shopping_list)

# lists are generally best to contain a single data type

## Dictionaries

contact_list = {
    "jane": "07541004844"
}

contact_list["bob"] = "04571685492"

contact_list["bob"] = "new number"

print(contact_list["jane"])
print(contact_list["bob"])

print(contact_list.keys())
print(contact_list.values())

#can use pop with a key to remove associated values

contacts = {
    "a": {
        "anne": "07541004844"
    },
    "b": {
        "brienne": "0123456789"
    },
    "c": {
        "charlie": "9876543210"
    }
}

# Get contacts within b key
print(contacts["b"].keys())
# Get Brienne's number
print(contacts["b"]["brienne"])



