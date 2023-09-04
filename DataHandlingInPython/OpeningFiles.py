# Working with files and error handling
import csv
# code is in multistring comments, comments are in #s

"""
file = open("order.txt")
"""

# FileNotFoundError: [Errno 2] No such file or directory: 'order.txt'

# open - built-in function that opens a file depending on the name of the file
'''
try:
    file = open("order.txt", "r")
    file_line_list = file.readlines()
    print(file_line_list)
    for line in file_line_list:
        list_of_words = line.split(', ')
        for word in list_of_words:
            print(word)
    # print(type(file_line_list)) Always useful to type check, especially jsons
    file.close()
except FileNotFoundError as msg:
    print('Error opening the file!')
    print(msg)
    raise
except SyntaxError:
    print('Syntax Error!')
'''
# try and except is a good way of avoiding errors, allows code to still run
# Can print the error message and error number by defining it
# Raise prints the error in full (the angry red text)

# Modes you can open a file in
# 'r'	This is the default mode. It Opens file for reading.
# 'w'	This Mode Opens file for writing. If file does not exist, it creates a new file.
# If file exists it truncates the file.
# 'x'	Creates a new file. If file already exists, the operation fails.
# 'a'	Open file in append mode. If file does not exist, it creates a new file.
# 't'	This is the default mode. It opens in text mode.
# 'b'	This opens in binary mode.
# '+'	This will open a file for reading and writing (updating)

# opening a file using with statements. you don't need to close at end
'''
try:
    with open("order.txt") as file:
        file_line_list = file.readlines()
        print(file_line_list)
        for line in file_line_list:
            list_of_words = line.split(', ')
            for word in list_of_words:
                print(word.strip())
except FileNotFoundError as msg:
    print('Error opening the file!')
    print(msg)
    raise
'''

# Opening csv files, don't need to install package, just import it
'''
with open("user_details.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)  # is a list of lists so can be iterated through, or cast to dictionary
    iterable_csv = iter(csvreader)
    next(iterable_csv)  # these lines together remove the frst row
    for row in iterable_csv:
        print(row)   
    print(list(csvreader))  # returns a list of lists
'''

# create a function to transform the data in a csv file


def transform_user_details(csv_filename):
    """
    Opens and transforms a csv file full of user details. The beginnings of data cleaning
    """
    new_user_data = []
    with open(csv_filename, newline='') as csvfile:
        user_details_csv = csv.reader(csvfile, delimiter=',')
        for user in user_details_csv:
            transformation = [user[1], user[2], user[-1]]  # first, last name and email
            new_user_data.append(transformation)

    return new_user_data


print(transform_user_details('user_details.csv'))


def create_new_user_details(old_filename="user_details.csv", new_filename="new_user_details.csv"):
    new_userdata = transform_user_details(old_filename)
    with open(new_filename, "w", newline='') as newfile:
        csv_writer = csv.writer(newfile)
        csv_writer.writerows(new_userdata)  # writerows for list of lists, writerow for list


create_new_user_details()
