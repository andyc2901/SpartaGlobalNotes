# Q1a: Print only the first 5 numbers in this list
print('Q1a')

x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
print(x[:5])

# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
print('Q1b')

answer = []
for N in range(len(x)):
    if x[N] % 2 == 0:
        answer.append(x[N])
print(answer)

# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
print('Q1c')

answer = []
for N in range(5):
    if x[N] % 2 == 0:
        answer.append(x[N])
print(answer)

# Q2a: from the list of names, create another list that consists of only the first letters of each first name
print('Q2a')

names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]
answer = []
for M in names:
    answer.append(M[0])
print(answer)

# Q2b: from the list of names, create another list that consists of only the index of the space in the string
print('Q2b')

answer = []
for M in names:
    answer.append(M.index(' '))
print(answer)

# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
print('Q2c')

answer = []
for M in names:
    N = [M[0], M[M.index(' ')+1]]
    answer.append(N)
print(answer)

# Q3a: Here is a list of lists, print only the lists which have no duplicates
print('Q3a')

list_of_lists = [[1, 5, 7, 3, 44, 4, 1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]
answer = []
for M in range(len(list_of_lists)):
    if len(list_of_lists[M]) == len(set(list_of_lists[M])):
        answer.append(list_of_lists[M])
print(answer)

# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered
print('Q4a')

answer = float(input('Input a number greater than 100'))
while answer < 100:
    answer = float(input('That iss less than 100. Try again'))
print(answer)