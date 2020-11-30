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

    open = []
    closed = [] 
    g_score = 0 

    # scores = {} 

    temp_h = manhatton(start, finish)
    node_start = Node(index= start, parent= None, g_score= g_score, h_score= temp_h)

    node_target = Node(finish, None, 0, 0)

    open.append(node_start)
    # scores[node_start.index] = node_start.cost

    while open:

        node_current = getCurrentNode(open) 

        if node_current.index == node_target.index: break

        # print(node_current.index)
        moves = validMoves(ROOM, node_current.index, ROOM_DIM)

        g_score += 1

        for move in moves: 
            node_successor = Node(index= move, parent= node_current, g_score= g_score, h_score= manhatton(move, finish))

            if node_successor not in open:
                if node_successor not in closed: 
                    open.append(node_successor)
                else: continue
            
            else: continue


        open.remove(node_current)
        closed.append(node_current)

    path = [] 
    while node_current.parent:
        path.append(node_current)
        node_current = node_current.parent
    
    return path

            


def getCurrentNode(open):

    temp = 99999 

    for node in open:
        if node.cost <= temp:
            currNode = node 
            temp = node.cost

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