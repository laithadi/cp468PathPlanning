# IMPORTS 
from utils import readTextFile, validRendezvousPoint
from aStarPathFinder import aStar 

# "welcome" message to indicate the start of the program 
print("\n\n\n")
print("Welcome to our Path Planning Term Project :)")
print("We are going to plan the paths for each robot. The hope is we can get them to the rendezvous point at night. The trick is to avoid any obstacles in the way. HERE WE GO ! ")
print("\n")

# calling the readTextFile() to grab all the important information from the input.txt file 
room_dim, robots, target_point, room = readTextFile() 

print("Room dimensions ==> {}\nNumber of robots and their starting coordinates ==> {}\nRendezvous point ==> {}\nThe museum:".format(room_dim,robots,target_point))
for row in room:
    print(row)
print("\n")
print("\n")
# find paths for robots only if the rendezvous point is valid (0) 
if validRendezvousPoint(room, target_point): 

    # list of keys in the robots dictionary
    robots_keys = robots.keys()  
    # storing all final paths for each robot
    all_paths = {}  
    # counter for naming the keys in all_paths
    i = 1   

    for key in robots_keys: 
        # starting tuple for the astar function is the value of the key in the robots dictionary
        current = robots[key] 
        # goal tuple for the astar() is the target (rendezvous) point
        goal = target_point  
        # calling aStar() and assigning the returned list to paths
        path = aStar(current, goal)  
        # adding the path for the robot in the all_paths 
        all_paths['Robot '+str(i)] = path 
        # increment i 
        i += 1 

    # list of keys for all_paths 
    ap_keys = all_paths.keys() 

    # printing the path for each robot
    for key in ap_keys:  
        # printing which robot the path belongs to 
        print("The path for {} is...\n".format(key)) 
        # retrieving the path list from all_paths
        pathlist = all_paths[key]
        # check to see if there is a way for the robot to get to the rendezvous point  
        if pathlist:
            # printing the index, g_score, h_score of each node 
            for node in pathlist:
                print("{}".format(node.index))
                print("\n")
                # f(n) = g(n) + h(n)
                print("g(n): {:>7}          h(n): {:>7}".format(node.g_score, node.h_score))
                print("\n")
            print("\n\n")
        # no path for robot       
        else:
            print("This robot couldn't make it :( ")
            print("\n\n")


    print("The end :) ") # the end 

# the rendezvous point is an obstacle itself so the robots cant get there 
else: 
    print("INVALID RENDEZVOUS POINT ... rendezvous point cannot be an obstacle itself  :( ")