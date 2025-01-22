

import random as r

import math as m

#Screen creation 

def screen_size(size):
    """ return two exact same dictionaries that are used for tracking
    what is on each coordinate of the display

    PreC: size>0 

    """
 
    screen={}

    screen_save={}


    for x in range(size):

        for y in range(size):
            screen[(y,x)]='0'
            screen_save[(y,x)]='0'

    screen[(0,0)]='*'
    screen_save[(0,0)]='0'

    return (screen, screen_save)


#screen displaying

def display(dic,size):
    """ Outputs the dictionary of the display as well
    the current user's location on it

    PreC: size>0 

    """
    

    lst=list(dic.values())

    n=size

    x = int(len(lst)/n)

    for y in range(0,len(lst),n):
        out=''
        for i in range(x):
        
            out+=lst[i+y]+' '
        print(out)


#Actions

def inspit(where):
    """ Returns a boolean that is used change the saved symbol of the dictionary display
    and indicates to the user that their current location
    does not match the randomly selected whereabouts of the treasure
    
    PreC:Where is a tuple
    """

    if where == treasure_is:
        print('')
        print('<-----You found a treasure----->')
        found=True

        
    elif where != treasure_is:
        print('<-----No treasure----->')
        found=False
    return found

def heat_map(xcord,ycord):
    
    xdifference = abs(treasure_x - xcord)
    ydifference = abs(treasure_y - ycord)

    print('X Heat is %s.'%xdifference)
    print('Y Heat is %s.'%ydifference)



lst=['1','2','3','4','5','6','7','8','9','0']
size_input_test=False

while size_input_test == False:
    count=0
    size= input('Enter the screen size nxn :')

    for x in size:
        print(x)
        if x in lst:
            count+=1
    if count==len(size):
        size_input_test=True
    else:
        print('Input Error %s is not a int'%size)
size=int(size)
#assert size>0,"Input is less then 0." # If the input is less then 0 screen_size and display Cease to function


treasure_x = r.randint(0,size-1)
treasure_y = r.randint(0,size-1)

treasure_is = ( treasure_x,treasure_y)

(screen,screen_save)= screen_size(size)



xcord = 0
ycord = 0
go=True

while go==True:

    display(screen,size)
    


    where = ( xcord, ycord)
    print(where)

    print()
    ask = input('1 is down | 2 is up | 3 is left | 4 is right|\
i to look | h to look at heat :')

    if ask == '4' and xcord!=size-1:
        screen[where]= screen_save[where]
        xcord+=1
        where = ( xcord, ycord)
        screen[where]='*'
    
    elif ask == '3' and xcord!=0:
        screen[where]= screen_save[where]
        xcord-=1
        where = ( xcord, ycord)
        screen[where]='*'
    
    elif ask == '1' and ycord !=size-1:
        screen[where]= screen_save[where]
        ycord+=1
        where = ( xcord, ycord)
        screen[where]='*'
    
    elif ask == '2' and ycord !=0:
        screen[where]= screen_save[where]
        ycord-=1
        where = ( xcord, ycord)
        screen[where]='*'
        
    elif ask == 'q':
        go=False
        
    elif ask == 'i':
        found=inspit(where)
        if found == False:
            screen_save[where]='x'
        
        
    elif ask == 'h':
        heat_map(xcord,ycord)



