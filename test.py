# from utils import readTextFile, validMoves, targetReached, strToInt
# from Astar import *
import random

# room_dim, robots, target_point, room = readTextFile() # calling the readTextFile() to grab all the important information from the input.txt file 

# # ----------------------------------------------This code right here is to just test and show that what the readTextFile() returns---------------------------------#
# print('This is the room dimensions: ')
# print(room_dim)
# print('\n')
# print("this is a dictionary of the robots and their starting points: ")
# print(robots)
# newrob = strToInt(robots)
# print(newrob)
# print('\n')
# print("this is the target point or rendezvous point: ")
# print(target_point)
# print('\n')
# print("this is the room in a 2d list:")
# #print(room)
# for i in range(0, int(room_dim[0])):
#     print(room[i])
# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------#
# # -----------------------------------------------------Testing the validMoves()-------------------------------------------------------------------#
# print('\n')
# moves = validMoves(room, (2,9), room_dim)
# print("Here are the valid moves robot 1 can make:")
# print(moves)
# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------#
# # ----------------------------------------------------------testing the targetReached()----------------------------------------------------------------------#
# notReached = targetReached(target_point, (3,1))
# reached = targetReached(target_point, (4,7))
# print('\n')
# print("This should return true or false depending on if the coordinates are the same: ")
# print(notReached)
# print(reached)
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------Testing the heuristic---------------------------------------------------------------------------#
# cent = (2,1)
# right = (3,1)
# left = (1,1)
# up = (2,0)
# down = (2,2)
# target = (4,7)

# print(manhatton(cent, target))
# print(manhatton(right, target))
# print(manhatton(left, target))
# print(manhatton(up, target))
# print(manhatton(down, target))
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------#


for i in range(0, 20):
    print('\n')
    for j in range(0, 25):
        print(random.randint(0,1), end='')