'''This program tells the user for the desecent speed, if the decent speed is 10 it is 
    considered to be a safe descent speed. '''

# Variables
speed = 0 
speed_list = []
safespeed = 10
stop = 'Final'

#Asking for Input
DS = input("Input descent speed in m/s: ")
while DS != stop:
    try:
        if DS.isnumeric():
            speed_list.append(int(DS)) #Putting user input into empty list
        else:
            print('Invalid score!')
        DS = input("Input descent speed in m/s: ")
    except ValueError:
        print('Invalid score!')
        
#Prints result

for item in speed_list:
    if item > 10:
        speed = speed + 1
if speed > 1: #output
    print(f'There were {speed} satelites faster than the safe speed')
