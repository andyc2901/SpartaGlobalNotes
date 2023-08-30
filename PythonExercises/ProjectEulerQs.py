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
        if is_palindrome(str(n*m)) == True:
            if n * m > ans:
                ans = n * m
        print(m)
        m += 1
    print(n)
    n += 1
    m = 900
print(ans)

# Q5: What is the smallest number that is divisible by every number from 1 to 20?

ints = [11,12,13,14,15,16,17,18,19,20]
check = 0
ans = 2520
while check != 11+12+13+14+15+16+17+18+19+20:
    check = 0
    x += 1
    for n in ints:
        if x % n == 0:
            check += n
    print(x)

