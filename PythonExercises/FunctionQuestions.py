# Python Function Questions from Paula to test our Knowledge

# Q1a: Write a function which takes in an integer as an argument,
# returns the divisors of that number as a list

print('Input a positive integer to find its factors')
number = int(input())


def find_factors(f):

    factors = []
    for N in range(int(f)):
        if f % (N+1) == 0:
            factors.append(N+1)
    return factors


print(find_factors(number))

# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise


print('input two positive integers')
number1 = int(input())
number2 = int(input())

if number1 > number2:
    factor_list = find_factors(number1)
    if number2 in factor_list:
        print(True, number2, 'is a factor of', number1)
    else:
        print(False, ', the numbers are not a factor of each other')

if number2 > number1:
    factor_list = find_factors(number2)
    if number1 in factor_list:
        print(True, number1, 'is a factor of', number2)
    else:
        print(False, ', the numbers are not a factor of each other')


# Q2a: write a function which takes a letter (as a string)
# as an input and outputs its position in the alphabet

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]


def alpha(letter):
    for M in range(len(alphabet)):
        if letter == alphabet[M]:
            return M+1


answer = alpha(input('Please input a letter'))
print(answer)

# Q2b: create a function which takes a persons name as an input string and returns an

first_name = input('Please input your first name')


def generate_id(name):
    ident = []
    for P in range(len(name)):
        ident.append(str(alpha(name[P])))
    ident = ''.join(ident)
    return ident


ID = generate_id(first_name)

print('ID:', ID)


# Q2c: Create a function which turns the ID into a password. The function should subtract
# the sum of the numbers in the id from the whole number of the id

def passcode(name):
    ident = generate_id(name)
    total = [int(ident) for ident in str(ident)]
    passw = int(ident) - sum(total)
    return passw


password = passcode(first_name)
print('Passcode:', password)


# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit


def is_prime(q):
    # A3b
    if float(q) % 1 != 0:
        return print('error, number is not an integer')
    elif int(q) < 0:
        return print('error, input is not positive')
    # A3b end
    factors = []
    for N in range(int(q)):
        if int(q) % (N + 1) == 0:
            factors.append(N + 1)
    no_of_factors = len(factors)

    if no_of_factors == 2:
        return print(q, 'is prime')
    else:
        return print(q, 'is not prime')


is_prime(input('Input a positive integer'))
