from restaurant import Table
from unittest import main

table01 = Table(5)
table01.order("Risotto", 12.50, 2)  # add 2 risotto and print
print(table01.bill)
table01.order("Burrito", 20.43, 3)  # add 3 burrito and print
print(table01.bill)
table01.order("Burrito", 20.43, 3)  # add 3 burrito and print
print(table01.bill)
table01.remove("Burrito", 20.43, 7)  # remove '7' burrito and print
print(table01.bill)
# table01.remove("Burrito", 20.43, 6)  # remove 6 burrito and print
print(table01.bill)
print(table01.get_subtotal())  # get the subtotal
print(table01.get_total(0.15))  # get the full total with a service charge of 15%
print(table01.split_bill())

# Run unit tests automatically
# main(module='test_module', exit=False)
