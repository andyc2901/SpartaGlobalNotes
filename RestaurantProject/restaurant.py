class Table:
    def __init__(self, number_of_customers):
        self.number_of_customers = number_of_customers
        self.bill = []

    def order(self, food: str, cost: float, quantity=1):

        if len(self.bill) == 0:
            self.bill.append({'item': food, 'price': cost, 'quantity': quantity})
        else:
            found = False
            for x in range(len(self.bill)):
                if self.bill[x]['item'] == food and self.bill[x]['price'] == cost:
                    found = True
                    self.bill[x]['quantity'] += quantity
            if found is False:
                self.bill.append({'item': food, 'price': cost, 'quantity': quantity})

    def remove(self, food: str, cost: float, quantity):
        if len(self.bill) == 0:
            return False
        for x in range(len(self.bill)):
            if self.bill[x]['item'] == food and self.bill[x]['price'] == cost:
                self.bill[x]['quantity'] -= quantity
                if self.bill[x]['quantity'] < 0:
                    self.bill[x]['quantity'] += quantity
                    return False
                elif self.bill[x]['quantity'] == 0:
                    self.bill.pop(x)
                    return True
                else:
                    return True

    def get_subtotal(self):
        subtotal = 0
        for x in range(len(self.bill)):
            subtotal += self.bill[x]['price'] * self.bill[x]['quantity']
        return round(subtotal, 2)

    def get_total(self,service_charge=0.1):
        subtotal = self.get_subtotal()
        sub_string = "{:,.2f}".format(subtotal)
        sub_string = '£' + sub_string
        service = round(subtotal * service_charge, 2)
        service_string = '£' + "{:,.2f}".format(service)
        total = subtotal + service
        total_string = '£' + "{:,.2f}".format(total)
        output = {'Sub Total': sub_string, 'Service Charge': service_string, 'Total': total_string}
        return output

    def split_bill(self):
        sub_total = self.get_subtotal()
        split_cost = sub_total/self.number_of_customers
        return split_cost
