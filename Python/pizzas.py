''' This program asks how many of each type of pizza should be ordered
    and then prints out the order, skipping any pizzas that weren't ordered '''
pizzas = ['cheese', 'chicken', 'pepperoni', 'veggie']
quantities = []

for pizza in pizzas:
    while True:
        try:
            howmany = int(input(f'How many {pizza} pizzas do we want? '))
            if howmany >= 0:
                break
            else:
                print('Please enter a valid amount')
        except ValueError:
            print('Please enter a valid amount')
    quantities.append(howmany)

for pizza, quantity in zip(pizzas, quantities):
    if quantity > 0:
        print(f'{pizza.capitalize()}: {quantity}')
