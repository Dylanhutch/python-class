########
#import modules
####### 
#the name of this game is the lost REVOLING ICE CREAM CONE
#you are in a very creepy house named the Hartman's manor looking the one and only ice cream cone 
#summary you are in the Hartman's manor loooking for his one and only revoling ice cream cone and you only have five moves to fint the room it is in there are 7 rooms in total 
# the only global varable is check_moves and it just tells you how many moves you have left
########
#define functions
#######
move = 6

def check_moves():
    global move
    move = move - 1  
    print("you have", move,"moves left" )
    if move <= 0:
        print("NO you didnt find the long lost treasure")
        sys.exit()


def start():
    print("Welcome!")
    room1()

def room1():
    check_moves()
    print("You are in Dining room")
    move = input("\nWhere would you like to go? Say one of these choices:\nBedroom\nbathroom\n")
    if move.lower() == "bedroom" or move.lower() == "Bedroom":
        room2()
    elif move.lower() == "bathroom" or move.lower() == "Bathroom":
        room5()
    else:
        print("Halt you cant go that way!!!!!!")
        pass

def room2():
    check_moves()
    print("You are in the bedroom")
    move = input("\nWhere would you like to go? Say one of these choices:\nkitchen\nlaundry room\n")
    if move.lower() == "kitchen" or move.lower() == "Kitchen":
        room4()
    elif move.lower() == "laundry room" or move.lower() == "Laundry room":
        room3()
    else:
        print("There is not time rest!!!!")
        pass

def room3():
    check_moves()
    print("You are in the laundry room")
    move = input("\nWhere would you like to go? Say one of these choices:\nkitchen\n")
    if move.lower() == "kitchen" or move.lower() == "Kitchen":
        room4()
    else:
        print("Are you trying to clean your clothes?")    
        pass

def room4():
    check_moves()
    print("You are in the kitchen")
    move = input("\nWhere would you like to go? Say one of these choices:\ndining room\n")
    if move.lower() == "Dining room" or move.lower() == "dining room":
        room1()
    else:
        print("Their isnt any food here so there is no point to stay")
        pass

def room5():
    check_moves()
    print("You are in the bathroom")
    move = input("\nWhere would you like to go? Say one of these choices:\nliving room\nbasement\n")
    if move.lower() == "living room" or move.lower() == "Living room":
        room6()      
    elif  move.lower() == "Basement" or move.lower() == "basement":
        room7()
    else:
        print("No time for showers") 
        pass   

def room6():
    check_moves()
    print("You are in the living room")
    move = input("\nWhere would you like to go? Say one of these choices:\nkitchen\n")
    if move.lower() == "kitchen" or move.lower() == "Kicthen":
        room4()
    else:
        print("You cant stay in here forever") 
        pass

def room7():
    print("YOU FOUND THE LENGDARY REVOLING ICE CREAM CONE. THIS IS LAST ICE CREAM CONE. yes it is very usless. also this is a real thing")

########
#main
#######
#TODO: Add some global variables

        
start()