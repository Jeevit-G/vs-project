veges = ["broccoli", "carrots", "beans", "peas", "cauliflower"] 
for vege in veges:
     print( vege )
choice = int( input( "Enter a number from 1 to 5" ))
vege_choice = veges[ choice - 1 ]
new_vege = input("What is your favourite vegetable? ")
if new_vege not in veges:
     veges.append( new_vege )

