## Numbers & operators

print(type(5))
print(type(5.50))

print(5 * 5.5)
print(type(5 * 5.5))  # put spaces between numbers, more readable

# modular operator returns the remainder from division

print(6 % 3)
print(6 % 4)

## Strings

print('Hello world')
print(type('hello world'))

print('a')
print(u'\u0061')

print('hello world'[1])
# [-1] gives the last index, error if you go to far in either pos or neg direction

print(len('hello world'))

##Booleans
'''
== equal to
!= not equal
> < less than greater than
>= <= less than or equal, greater than or equal
'''
# can compare integers and floats, but can't compare strings and numbers
print(4 == 4)
print(3 != 4)
print(3 > 4)
print(3 < 4)

print(2 == len('2'))

# Truthy or Falsey

print(bool(2))
print(bool(0))
# anything other than 0 is true!
# Empty strings are false, any string with a character in is true
