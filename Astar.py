def Astar(current, goal, heuristic):
    """
    Takes the current state of the robots in the musuem
    and returns the path they take to get to the goal state
    using the Manhatton distance heuristic
    """

def manhatton(current, goal):
    """
    Calculates the best choice for each move
    """
    length = len(current)
    manhatton = 0

    for x in range(length):
        for y in range(length):
            #to ignore the empty tile
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