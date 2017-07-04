class ShoppingCart():
    """ shoppingcart for a supermarket point of sales"""
    def __init__(self):
        self.total = 0
        self.items ={}
    
    def add_item(self, item_name, quantity, price):
        """ Function for adding items in the cart"""
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items.update({item_name:quantity})
          
        self.total += (price*quantity)
        
    def remove_item(self, item_name, quantity, price):
        """ Function for removing items from the cart """
        if len(self.items.keys()) > 0: 
            if self.items[item_name] < quantity:
                self.total -= (price * self.items[item_name])
                del self.items[item_name]
            else:
                self.items[item_name] -= quantity
                self.total -= price * quantity
                
    def checkout(self, cash_paid):
        """ Function for checking out """
        balance = 0
        if cash_paid > self.total:
            balance = (cash_paid - self.total)
            return balance
        else:
            return 'Cash paid not enough'   

class Shop(ShoppingCart):
    """ Shop class demonstrating inheritance """
    def __init__(self):
        self.quantity = 100
    def remove_item(self):
        self.quantity -= 1
