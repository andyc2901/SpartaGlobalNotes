class Person:
    def __init__(self, fname, lname):
        self._first_name = fname
        self._last_name = lname

    # Can create a print function that displays the full name of the customer when called.
    # Only if firstName and lastName are defined in the __init__ clause like the second option:

    def print(self):
        print(f'Full name: {self._first_name} {self._last_name}')

    # Can use a decorater to provide info about classes and how they're intended to be used

    @property
    # defined to recall (get) first name
    def first_name(self):
        print('In get method')
        return self._first_name

    @first_name.setter
    # designed to change (set) first name
    def first_name(self, new_first_name):
        print('In set method')
        self._first_name = new_first_name
