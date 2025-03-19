''' This program asks how many of each type of pizza should be ordered
    and then prints out the order, skipping any pizzas that weren't ordered '''

# Create list of pizza types
pizzas = ['cheese ', 'chicken', 'pepperoni', 'veggie']
# Create list to store how many of each pizza
quantities = []

# Go through list of pizzas in order
for pizza in pizzas:
    # Ask how many of each pizza
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

# Go back through all the pizzas
for pizza, quantity in zip(pizzas, quantities):
    # Only print when quantity is greater than 0
    if quantity > 0:
        print(f'{pizza.capitalize()}: {quantity}')
