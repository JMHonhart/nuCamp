'''Icecream Shop CC'''


class Queue:
    '''Queue Class'''

    def __init__(self):
        self.items = []

    def size(self):
        '''Size of'''
        return len(self.items)

    def enqueue(self, item):
        '''add Item'''
        self.items.append(item)

    def dequeue(self):
        '''Remove Item'''
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        '''Show'''
        print(self.items)

class IceCreamShop:
    '''Shop Class'''

    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        '''Order'''
        if flavor not in self.flavors:
            print("Sorry, we dont have that flavor")
            return
        if scoops < 1 or scoops > 3:
            print("Choose between 1-3 scoops")
            return
        print("Order created!")
        order = {"customer": customer, "flavor": flavor, "scoops": scoops}
        self.orders.enqueue(order)

    def show_all_orders(self):
        '''Show all'''
        print("\nAll Pending Ice Cream Orders:")

        for order in self.orders.items:
            print("Customer:", order["customer"], "-- Flavor:", order["flavor"], "-- Scoops:", order["scoops"])    
                
    def next_order(self):
        '''Next '''
        print("\nNext Order Up!")
        order = self.orders.dequeue()
        print("Customer:", order["customer"], "-- Flavor:", order["flavor"], "-- Scoops:", order["scoops"])

shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()