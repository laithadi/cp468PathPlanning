import copy
from utils import validMoves, readTextFile

ROOMDIM, _, TARGET_POINT, ROOM = readTextFile()

def Astar(current, goal):
    """
    Takes the current state of the robots in the musuem
    and returns the path they take to get to the goal state
    using the Manhatton distance heuristic
    """
    curr_state = copy.deepcopy(current)
    goal_state = copy.deepcopy(goal)

    poss_moves = []
    open_list = []
    closed_list = []
    g_score = 0
    f_score = 9999

    # append the current state of the node into the open list
    open_list.append(current)
    
    # Run this loop whil there is still possible moves in the list.
    while len(open_list)> 0:
        currIndex = 0
        currNode = open_list[0] #our current Node
        closed_list.append(currNode)
        moves = validMoves(ROOM, currNode,ROOMDIM ) #switch validmoves to only take tmep which is the current node.

        for index, move in enumerate(open_list): #Might not need this
            print("Current {}, goal {}".format(move, goal))
            if (int(g_score + manhatton(move, goal))) < int(g_score + manhatton(currNode, goal)):
                currNode = move
                currIndex = index

        open_list.pop() #pop off old move
        closed_list.append(currNode) #Add best value to our closed list

        for index, move in enumerate(moves):
            temp_score = int(g_score + manhatton(move, goal))
            if move not in closed_list:
                if temp_score < f_score: #Compare the closest node
                    currNode = move #Assign our best move to currNode
                    currIndex = index
                    f_score = temp_score
        open_list.append(currNode)
            
            

        if currNode == goal:
            return closed_list
        else:
            g_score += 1
        
        



def manhatton(current, goal):
    """
    Calculates the best choice for each move
    """
    
    currX = current[0]
    currY = current[1]

    goalX = goal[0]
    goalY = goal[1]

    return abs(goalX - currX) + abs(goalY - currY)


def get_index(array, value):

    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == value:
                return (i, j)
    return -1, -1