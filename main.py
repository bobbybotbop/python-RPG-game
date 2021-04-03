import time


starttime=time.time() 

candyRate = 1
candy = 0
lolli = 0

def showInstructions():
    #print a main menu and the commands 

#removed "candy : [count, eat, drop]"

    print('''
  Candy Box
  ========
  Commands:
    go [up, down, left, right]
    map [house]

  dont get lost!!  (u have to restart ur game)
__________________________________________
  ''')
    print('''
    map of house: 


                     door to outside
 +---------+-----------+________+-----------+             
 | snack   |    \033[1;32;40m--o\033[0m                grandma's|             
 |  \033[1;36;40m--o\033[0m     |  kitchen                room   |             
 |  \033[1;34;40m--o\033[0m    |    \033[1;31;40m--o\033[0m                         |             
 +---------+------------+      +------------+             
                       |   h  |                       
                       |   a  |                      
                       |   l  |                       
                       |   l  |                      
                       |      |                       
                +------+      +------+--------+                   
                |                    |bathroom|           
                |      your room     |        |           
                |                    |        |           
                +--------------------+--------+                 ''')


def showStatus(candyRate, candy):
#starts the game with 0 candy
 #idk why but it only works when i put it here 

#the lolli system that is supposed to increase the candy rate isnt working soo.. imma just comment it out for now

#  if lolli >= 0:
#    candyRate += lolli

  #item system 
  if "item1" in rooms[currentRoom]:
      print('you see a ' + rooms[currentRoom]['item1'] + '!')
#      lolli += 1

  if "item2" in rooms[currentRoom]:
      print('you see a ' + rooms[currentRoom]['item2'] + '!')
#      lolli += 1

#candy counter
  if candy >= 0:
    candy += (round((time.time() - starttime)) * candyRate)
    
#basic ui

  print(
      '\n=========================================================================='
  )
  print('You are in ' + currentRoom)

  print('Candies :  ' + str(candy) + '                                        Candy rate: ' + str(candyRate) + ' per sec')
  print(
      "==========================================================================")

  

#a dictionary linking a room to other rooms
rooms = {
    'Your Room': 
    {
        'up': 'Hall',
        'right': 'Bathroom'
    },
    'Bathroom':
    {
      'left' : 'Your room',
    },

    'Hall': 
    {
        'down': 'Your Room',
        'right': 'Grandmas Room',
        'left': 'Kitchen',
        'up' : 'door'
    },
    'Grandmas Room': 
    {
        'left': 'Hall'
    },
    'Kitchen': 
    {
        'right': 'Hall',
        'left' : 'Snack Place',
        'item1' : 'Green lollipop',
        'item2' : 'Red lollipop'
    },
    'Snack Place':
    {
      'right' : 'Kitchen',
      'item1' : 'Cyan lollipop',
      'item2' : 'Blue lollipop'
    },
    'door' :
    {
      'up' : 'outside',
      'down' : 'Hall'
    },

    'outside':
    {
      'up' : 'a bit lost',
      'down' : 'door',
      'left' : 'a bit lost',
      'right' : 'a bit lost'
    },
    'a bit lost':
    {
      'up' : 'very very lost',
      'down' : 'outside',
      'left' : 'a bit more lost',
      'right' : 'very lost'
    },
    'very very lost':
    {},
    'a bit more lost':
    {},
    'very lost':
    {},

}

#start the player in your room
currentRoom = 'Your Room'


showInstructions()


while True:

#    candy = 0 # again idk why but im gonna put this here again prob not the best way to do this
#    if candy >= 0:
#        candy += (round((time.time() - starttime)) * candyRate)

    showStatus(candyRate, candy)
    

    move = ''
    while move == '':
        move = input('')

    move = move.lower().split()

#movemint system
    if move[0] == 'go':

        if move[1] in rooms[currentRoom]:

            currentRoom = rooms[currentRoom][move[1]]

        else:
            print('you cant go that way!')

#map System
    if move[0] == "map":

        if move[1] == "house":
              print('''
    map of house: 


                     door to outside
 +---------+-----------+________+-----------+             
 | snack   |    \033[1;32;40m--o\033[0m                grandma's|             
 |  \033[1;36;40m--o\033[0m     |  kitchen                room   |             
 |  \033[1;34;40m--o\033[0m    |    \033[1;31;40m--o\033[0m                         |             
 +---------+------------+      +------------+             
                       |   h  |                       
                       |   a  |                      
                       |   l  |                       
                       |   l  |                      
                       |      |                       
                +------+      +------+--------+                   
                |                    |bathroom|           
                |      your room     |        |           
                |                    |        |           
                +--------------------+--------+                 ''')

#candy System

    if move[0] == "candy":

        if move[1] == "count":
          print()

