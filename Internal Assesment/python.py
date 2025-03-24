'''This program tells the user for the desecent speed, if the desecent speed is 10 it is 
    considered to be a safe descent speed. '''

# These are the variables used in the program
speed = 0 
speed_list = [] 
high_list = []
safespeed = 10
stop = 'final' # Used to end the code

#Asking for Input
DS = input("Input descent speed in m/s: ")
while DS != stop:
    try:
        if DS.isnumeric(): #Checks if the input is a numeric
            speed_list.append(float(DS)) #Putting user input into empty list

        
        else:
            print('Invalid descent speed!') # If not numeric it prints this and asks to try again
        DS = input("Input descent speed in m/s: ")
    except ValueError:
        print('Invalid descent speed!')
        
#This block of program prints out the results

for item in speed_list:
    if item > 10:
        speed = speed + 1
        high_list.append(float(item))

if speed > 1: #output
    print(f'There were {speed} satellites faster than the safe speed.') # Plural 
    print('The unsafe speeds are')
    for n in high_list:
        print(n)

elif speed == 1: 
    print(f'There was {speed} satellite faster than the safe speed.')  # Non Plural
    print('The unsafe speeds are')
    for n in high_list:
        print(n)

else:
    print(f'There were {speed} satellite faster than the safe speed.')
