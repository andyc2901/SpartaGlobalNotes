## While loops

# loops for a boolean so long as it is true

counter = 0

while counter < 10:
    if counter % 2 == 0:
        print(counter)
    else:
        print("odd")
    counter += 1

## For Loops

# dependant on iterables

#do they hold more than one data type?

example_string = "test"

basket = ["eggs","bread"]
for basket_item in basket:
    print(basket_item)

customers = {
    "name": "tess",
    "age": 25
}
for customer in customers.values():
    print(customer)
