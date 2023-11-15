"""defining a class!"""

from __future__ import annotations


class pizza:
    """rgus us nt ckass to present pizza"""

    #attributes
    #syntax <name> : <type>
    sizes: str
    toppings: int
    gluten_free: bool

    def __init__(self, size_input: str, toppings_input: int, gf_input: bool):
        """Constructor"""
        self.size = size_input
        self.toppings = toppings_input
        self,gluten_free = gf_input
        # return self


    def price(self) -> float:
        """method to compyte price of pizza"""
        if self.size =="large":
            cost: float = 6.25
        else:
            cost: float = 5.00
        cost += .75 * self.toppings
        if self.gluten_free:
            cost += 1.00
        return cost
    
    def add_toppings(self, num_toppings: int):
        """unpdate existing pizza order w num_toppings"""
        self.toppings = self.toppings + num_toppings

    def add_toppings_new_order(self, num_toppings: int) -> pizza:
            """"make new pizza order using existing info"""
            new_pizza: pizza = pizza(self.size, self.toppings + num_toppings, self.gluten_free)
            return new_pizza