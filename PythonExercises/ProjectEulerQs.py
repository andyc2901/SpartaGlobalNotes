# Q1: find the sum of all multiples of 5 below 1000
x = 1
total = 0
while x < 1000:
    if x % 3 == 0:
        total += x
    elif x % 5 == 0:
        total += x
    x += 1
print(total)

# Q2: find the sum of all even fibonacci numbers below 4000000

x = 1
y = 2
z = 3
total = 2
while z < 4000000:
    z = x + y
    if z % 2 == 0:
        total += z
    x = y
    y = z
print(total)

# Q3: What is the largest prime factor of 600851475143

n = 600851475143
i = 2
while i * i < n:
    while n % i == 0:
        n = n / i
    i = i + 1
print(n)

# Q4: What is the largest palindrome made by the multiplication of two 3-digit numbers


def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False


n = 900
m = 900
ans = 0
while n < 1000:
    while m < 1000:
        if is_palindrome(str(n*m)) == 1:
            if n * m > ans:
                ans = n * m
        print(m)
        m += 1
    print(n)
    n += 1
    m = 900
print(ans)

# ##
# Q5: What is the smallest number that is divisible by every number from 1 to 20?
#
#  brute force :'|
#
# ints = [11,12,13,14,15,16,17,18,19,20]
# check = 0
# ans = 2520
# while check != 11+12+13+14+15+16+17+18+19+20:
#     check = 0
#     x += 1
#     for n in ints:
#         if x % n == 0:
#             check += n
#     print(x)
# ##
# Q6: difference between sum of squares and square of sums of first 100 numbers

sum_of_squares = 0
square_of_sum = 0
x = 0
while x <= 100:
    sum_of_squares += x**2
    square_of_sum += x
    x += 1
ans = (square_of_sum**2) - sum_of_squares
print(ans)

# Q7: What is the 10,001st prime number?


def is_prime(p):
    count = 0
    for q in range(int(p**0.5)):
        if p % (q+1) == 0:
            count += 1
    if count == 1:
        return True
    else:
        return False


primes = []
z = 1
while len(primes) <= 10001:
    if is_prime(z) == 1:
        primes.append(z)
    z += 1
print(primes[-1])

# Q8: Greatest sum of 13 consecutive digits in a 1000-digit number

numb = ('''7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607
8911294949545950173795833195285320880551112540698747158523863050715693290963295227443043557668966489504452445231617
31856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930
79608667017242712188399879790879227492190169972088809377665727333001053367881220235421809751254540594752243525849077116
70556013604839586446706324415722155397536978179778461740649551492908625693219784686224828397224137565705605749026140797
29686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042242190226710556263211111093705442175069416589604080719840385096245544
43629812309878799272442849091888458015616609791913387549920052406368991256071760605886116467109405077541002256983155200
05593572972571636269561882670428252483600823257530420752963450'''.replace("\n", ""))
ans = 0
for h in range(len(numb)-13):
    prod = 1
    for g in range(13):
        prod *= int(numb[h+g])
    if prod > ans:
        ans = prod
print(ans)
