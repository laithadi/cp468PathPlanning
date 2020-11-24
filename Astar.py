import copy
from utils import validMoves

def Astar(current, goal, heuristic):
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
    while len(open_list > 0):
        temp = open_list[0]
        moves = validMoves(temp) #switch validmoves to only take tmep which is the current node.
        for move in moves:
            temp_score = int(g_score + manhatton(move, goal))
            if temp_score < f_score:
                f_score = temp_score
        



def manhatton(current, goal):
    """
    Calculates the best choice for each move
    """
    length = len(current)
    manhatton = 0

    for x in range(length):
        for y in range(length):
            if current[x][y] != 0 or current[x][y] != 0:
                (goalx, goaly) = get_index(goal, current[x][y])
                manhatton += abs(x - goalx) + abs(y - goaly)
    return manhatton


def get_index(array, value):

    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == value:
                return (i, j)
    return -1, -1