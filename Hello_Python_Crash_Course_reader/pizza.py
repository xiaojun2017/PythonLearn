pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
print('you ordered a ' + pizza['crust'] + '-crust pizza' + " with the following toppings:")
for topping in pizza['toppings']:
    print(topping, end=" ")
