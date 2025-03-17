'''This prograsm asks the user of how many of each pizza should be ordered
and prints out the order while skipping the ones that has the values of 0'''

pizza_li = [] # is an empty list that is going to store input

minimum = 0 # makes a minimum variable



while True:
    try:
        cheese = input('How many cheese pizzas do we want? ')
        cheese = int(cheese)
        if cheese < minimum:
            print('Please enter a valid input ')
        
        else:
            pizza_li.append(cheese)
            break 
    except ValueError: # if the value doesn't match the required value its going to print:
        print('Please enter a valid input')

while True:
    try:
        chicken = input('How many chicken pizzas do we want? ')
        chicken = int(chicken)
        
        if chicken < minimum:
            print('Please enter a valid input ')
        
        else:
            pizza_li.append(chicken)
            break
    except ValueError: # if the value doesn't match the required value its going to print:
        print('Please enter a valid input')

while True:
    try:
        pepperoni = input('How many pepperoni pizzas do we want? ')
        pepperoni = int(pepperoni)

        
        if pepperoni < minimum:
            print('Please enter a valid input ')
        
        else:
            pizza_li.append(pepperoni)
            break
    except ValueError: # if the value doesn't match the required value its going to print:
        print('Please enter a valid input')
while True:
    try:
        veggie = input('How many veggie pizzas do we want? ')
        veggie = int(veggie)
        if veggie < minimum:
            print('Please enter a valid input ')
        
        else:
            pizza_li.append(veggie)
            break
    except ValueError: # if the value doesn't match the required value its going to print:
        print('Please enter a valid input')

for i in range(0, 1): #this is going to print out the order of pizzas
    if pizza_li[0] != minimum:
        print(f'Cheese: {pizza_li[0]}')
    if pizza_li[1] != minimum:
        print(f'Chicken: {pizza_li[1]}')
    if pizza_li[2] != minimum:
        print(f'Pepperoni: {pizza_li[2]}')
    if pizza_li[3] != minimum:
        print(f'Veggie: {pizza_li[3]}')




        

