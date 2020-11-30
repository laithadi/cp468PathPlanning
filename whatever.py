from utils import * 

ROOM_DIM, _, TARGET_POINT, ROOM = readTextFile()

class Node:

    def __init__(self, index, parent, g_score, h_score):
        self.index = index
        self.parent = parent
        self.g_score = g_score
        self.h_score = h_score
        self.cost = h_score + g_score 



def aStar(start, finish):

    open_list = [] # node that we have NOT explored its moves 
    closed_list = [] # nodes that we have explored its moves
    g_score = 0  # the depth we add to the total cost 

    temp_h = manhatton(start, finish) # heuristic of the start node 
    node_start = Node(index= start, parent= None, g_score= g_score, h_score= temp_h) # node of the start position

    node_target = Node(finish, None, 0, 0) # node for the rendezvous point

    open_list.append(node_start) # adding the starting position node to the open_list 

    while open_list: # as long as we have a node in the open_list

        node_current = getCurrentNode(open_list) # select the node with the least cost in open_list 

        if node_current.index == node_target.index: break # if we reached the rendezvous point, break 

        moves = validMoves(ROOM, node_current.index, ROOM_DIM) # get all the valid moves 

        g_score += 1 # increase the g_score by 1 as we expand the node_current 

        for move in moves: # for each move in the valid move for node_current 
            node_successor = Node(index= move, parent= node_current, g_score= g_score, h_score= manhatton(move, finish)) # create node for child of node_current

            if node_successor.index == node_target.index: return "YAY"


            if node_successor not in open_list: # we have not come accross this node 
                if node_successor not in closed_list:  
                    open_list.append(node_successor) # add to the open_list 
                else: continue
            
            else: continue


        open_list.remove(node_current) # remove the node_current to not visit it again 
        closed_list.append(node_current) # to keep track of nodes expanded 

    path = [] # the path 
    while node_current.parent: # while there exists a node to back track 
        path.append(node_current) # add node to path 
        node_current = node_current.parent # move on to the next node 
    
    return path 

            


def getCurrentNode(open_list):
    """
    returns the node with the lowest cost 
    """

    temp = 99999 

    for node in open_list: # each node in the open_list
        if node.cost <= temp: # if the cost of the node is less than temp 
            currNode = node  # node becomes the new currNode 
            temp = node.cost # temp gets updated to the currNode cost 

    return currNode 




def manhatton(current, goal):
    """
    Calculates the best choice for each move
    """
    
    currX = current[0]
    currY = current[1]

    goalX = goal[0]
    goalY = goal[1]

    return abs(goalX - currX) + abs(goalY - currY)