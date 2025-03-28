'''This program tells the user for the desecent speed, if the desecent speed is 10 it is 
     considered to be a safe descent speed. '''
 
# These are the variables used in the program
speed = 0 
mini = 0
speed_list = [] # Creates an empty list
max = 10
stop = 'final' # Used to end the code

#Asking for Input
word = input("Input descent speed in m/s: ")
while word != stop:
    try:
        word = word.lower()
        if word.replace(".", "").isnumeric(): #Checks if the input is a numeric if float is replaces the decimal with blank
            speed_list.append(float(word)) #Putting user input into empty list and floats it
        else:
            print('Error, invalid input.') # If not numeric it prints this and asks to try again
        word = input("Input descent speed in m/s: ")
        word = word.lower()
    except ValueError:
        print('Error, invalid input.') # If error it prints
 
 #This block of program prints out the results
 
for item in speed_list:
    if item > max:
        speed = speed + 1
print(f'There were {speed} satellites faster than the safe speed.') 
if speed > mini: #output
    print('The unsafe speeds are')
    for item in speed_list:
        if item > max:
            print(item)

