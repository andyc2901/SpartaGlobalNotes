# File to play fizz buzz with python

def fizzbuzz(number: int):
    x = 1
    while x <= number:
        if x % 3 == 0 and x % 5 == 0:
            print('FizzBuzz')
        elif x % 3 == 0 and x % 5 != 0:
            print('Fizz')
        elif x % 3 != 0 and x % 5 == 0:
            print('Buzz')
        else:
            print(x)
        x += 1


fizzbuzz(int(input('input an integer to play fizzbuzz up to ')))
