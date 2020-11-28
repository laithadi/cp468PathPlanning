from utils import readTextFile, validMoves, targetReached, strToInt

room_dim, robots, target_point, room = readTextFile() # calling the readTextFile() to grab all the important information from the input.txt file 

# ----------------------------------------------This code right here is to just test and show that what the readTextFile() returns---------------------------------#
print('This is the room dimensions: ')
print(room_dim)
print('\n')
print("this is a dictionary of the robots and their starting points: ")
print(robots)
newrob = strToInt(robots)
print(newrob)
print('\n')
print("this is the target point or rendezvous point: ")
print(target_point)
print('\n')
print("this is the room in a 2d list:")
#print(room)
for i in range(0, int(room_dim[0])):
    print(room[i])
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------#
# -----------------------------------------------------Testing the validMoves()-------------------------------------------------------------------#
print('\n')
moves = validMoves(room, robots[1], room_dim)
print("Here are the valid moves robot 1 can make:")
print(moves)
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------testing the targetReached()----------------------------------------------------------------------#
notReached = targetReached(target_point, (3,1))
reached = targetReached(target_point, (4,7))
print('\n')
print("This should return true or false depending on if the coordinates are the same: ")
print(notReached)
print(reached)
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------#