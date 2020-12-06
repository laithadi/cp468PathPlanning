# IMPORTS 
from utils import readTextFile, validMoves
from node import Node

# GLOBAL VARIABLES 
ROOM_DIM, _, TARGET_POINT, ROOM = readTextFile()


def aStar(start, finish):
    """
    parameters:
        start: a tuple (i,j) of the starting coodinates of the robot. 
        finish: a tuple (i,j) of the rendezvous point for the robot.

    returns: 
        path: a list of tuple [(i,j), (l,k),..]. 
            the tuples are coordinates the robot must take in order to get to the finish. 
            the list is all the coordinates together. 
    """

    # node that we have NOT explored its moves 
    open_list = [] 
    # nodes that we have explored its moves
    closed_list = [] 
    # the depth we add to the total cost
    g_score = 0  

    temp = True 

    # heuristic of the start node
    h_score_start_node = manhatton(start, finish)  
    # creating the node for the start coordinate 
    node_start = Node(index= start, parent= None, g_score= g_score, h_score= h_score_start_node)

    # node for the rendezvous point
    node_target = Node(finish, None, 0, 0) 

    # adding the starting position node to the open_list
    open_list.append(node_start)  

    # as long as we have a node in the open_list
    while open_list and temp: 

        # select the node with the least cost in open_list 
        node_current = getCurrentNode(open_list) 

        # if we reached the rendezvous point, break
        if node_current.index == node_target.index: break  

        # get all the valid moves 
        moves = validMoves(ROOM, node_current.index, ROOM_DIM) 
        # increase the g_score by 1 as we expand the node_current
        g_score += 1  

        # for each move in the valid move for node_current
        for move in moves:   
            # create node for child of node_current
            node_successor = Node(index= move, parent= node_current, g_score= g_score, h_score= manhatton(move, finish)) 

            # check if the successor the target point 
            if node_successor.index == node_target.index: 
                temp = False
                break

            # we have not come accross this node or expanded it 
            if (not inOpen(node_successor, open_list)) and (not inClosed(node_successor, closed_list)): 
                # add to the open_list
                open_list.append(node_successor) 

        # remove the node_current to not visit it again 
        open_list.remove(node_current) 
        # to keep track of nodes expanded 
        closed_list.append(node_current) 

    # if open_list is not empty, that means we broke out of the while loop cause we reached the target point 
    if open_list: 
        # backtrack to append all the nodes in a list for the path 
        path = [] 
        while node_current.parent: # while there exists a node to back track 
            path.append(node_current) # add node to path 
            node_current = node_current.parent # move on to the next node 
        
        # reverse the path 
        path.reverse()

        return path 
    
    # open_list is empty, means that we exhausted all of our options and no path has been found
    else: 
        return []


def getCurrentNode(open_list):
    """
    parameters:
        open_list: a list (node1, node2, ...).
                a list of all the nodes that have yet to be explored.
    
    returns:
        currNode: a Node() with the lowest node.cost in open_list. 
    """

    temp = 99999 

    # each node in the open_list
    for node in open_list: 
        # if the cost of the node is less than temp 
        if node.cost <= temp: 
            # node becomes the new currNode 
            currNode = node  
            # temp gets updated to the currNode cost 
            temp = node.cost 

    return currNode 


def inOpen(node, open_list):
    """
    parameters:
        node: Node() we are checking to see if it is in the open_list. 
        open_list: a list of Node() that have yet to be explored. 
    
    returns: 
        boolean: True if node is in open_list. 
                 False otherwise.
    """

    # index of the node 
    ind = node.index

    # going through the nodes in the open_list 
    for n in open_list:
        # if the index of the node is the same as ind, then the node is in open_list 
        if n.index == ind: return True 

    return False 


def inClosed(node, closed_list):
    """
    parameters:
        node: Node() we are checking to see if it is in the closed_list. 
        closed_list: a list of Node() that have already explored. 
    
    returns: 
        boolean: True if node is in closed_list. 
                 False otherwise.
    """

    # index of the node 
    ind = node.index

    # going through the nodes in the closed_list
    for n in closed_list:
        # if the index of the node is the same as ind, then the node is in closed_list
        if n.index == ind: return True 

    return False



def manhatton(current, goal):
    """
    parameters: 
        current: a tuple (i,j) of the coordinate we are calculating the manhatton of.
        goal: a tuple (i,j) of the rendezvous point.
    
    returns: 
        the manhattan value. (int)
    """
    
    # get the x and y coordinates of the current point
    currX = current[0]
    currY = current[1]

    # get the x and y coordinates of the rendezvous point 
    goalX = goal[0]
    goalY = goal[1]

    return abs(goalX - currX) + abs(goalY - currY)