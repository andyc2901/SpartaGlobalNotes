# Abstraction: Creating and using classes
import customer
import employee
import random

cust = customer.Customer('Matt', 'Carver', 'Norwich')
cust.print()

# Encapsulation

# There is currently nothing stopping us changing the customers details, violates encapsulation
# No real way of enforcing encapsulation in python, but can use conventions to prevent it
# Any property starting with an underscore should be considered a private feature
# not intended for use with other pieces of code
cust.first_name = 'Matt'
cust.print()

# Inheritance

# right click, refactor, pull members up to take all details from customer class and input them into person class
# The code here still works as all the person class details are still part of customer class as customer class is
# a subclass of person class

emp = employee.Employee('Jeff', 'Stirling', 'presenter')
emp.print()

# Polymorphism

# Already done in previous example! print from cust and from emp use the same command to get different answers
# Program looks for the most specific version of the function available.
# Starts at the bottom of inheritance hierarchy, and goes to top. If none, throws error

if random.randint(0,1)== 0:
        my_person = customer.Customer('Matt', 'Carver', 'Norwich')
else:
        my_person = employee.Employee('Jeff', 'Stirling', 'presenter')
my_person.print()
# No way of knowing which version of print function will run, but both are available until the randint is called
