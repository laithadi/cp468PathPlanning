from utils import *
from Astar import *
from whatever import * 

print("Welcome to our Path Planning Term Project :)")

room_dim, robots, target_point, room = readTextFile() # calling the readTextFile() to grab all the important information from the input.txt file 

print(room_dim)

robots = strToInt(robots) # turn all values in the robots value to int 
r_keys = robots.keys() # grab all the keys in the robots dictionary 

all_paths = {} # dictionary we are storing all final paths for each robot 
i = 1  # counter just for naming the keys in the all_paths dictionary 

for key in r_keys: 
    current = robots[key] # setting the starting tuple for the astar function 
    goal = target_point # the goal for the astar() is the target point 
    print('start')
    path = aStar(current, goal) # calling the astar() and assigning the returned list to paths 
    print("done")
    all_paths['Robot'+str(i)] = path # adding the path for the robot in the all_paths dictionary for the right key naming 
    i += 1 # add one to i so next time we name the key for the robots path, its the right robot

ap_keys = all_paths.keys() # getting all the keys for all_paths 

for key in ap_keys: # this for loop just goes through the all_paths dictionary and prints each path 
    print("The path for {} is...\n".format(key)) 
    pathlist = all_paths[key]
    for node in pathlist:
        print(node.index)
    print('\n')


print("Success, all robots have reached the rendezvous point :) ") # the end 