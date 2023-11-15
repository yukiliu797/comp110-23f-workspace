""" Instantiating a class."""
from lessons.pizza import pizza


my_pizza: pizza = pizza("large", 10, True) #constructor

#acess/set/update attribute values
#my_pizza.sizes = "large"
#my_pizza.toppings = 10
#my_pizza.gluten_free = True
my_pizza.toppings +=2

print("Size: ")
print(my_pizza.sizes)
print(my_pizza.toppings)

#print("my_pizza: ")
#print(my_pizza)

#make sals_pizza size medium, 5 toppings, not gF
sales_pizza: pizza = pizza("medium", 5, False)
print(sales_pizza.size)

def price(input_pizza: pizza) -> float:
    if input_pizza.size =="large":
        cost: float = 6.25
    else:
        cost: float = 5.00
    cost += .75 * input_pizza.toppings
    if input_pizza.gluten_free:
        cost += 1.00
    return cost

print(price(my_pizza))
print(price(sales_pizza))

#calling method
print(my_pizza.pice())
print(sales_pizza.pice())

my_pizza.add_toppings(3)
print(my_pizza.toppings)
print(my_pizza.pice())

my_second_pizza: pizza = my_pizza.add_toppings_new_order(2)
print(my_second_pizza.toppings)
print(my_pizza.toppings)