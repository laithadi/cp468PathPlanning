def readTextFile():
    """
    Reads the input.txt file and returns the room dim (tuple), robots and their starting positions (dictionary),
    target point (tuple), room (2d list)
    """
    f = open("input.txt", "r") # opening input.txt file to access the information 

    lines = f.readlines() # reads every line in input.txt file stores each line in a list 

    room_dim = lines[0].split(" ") # the dimensions of the room in a list data type 
    room_dim[0] = int(room_dim[0])
    room_dim[1] = int(room_dim[1])
    room_dim.remove('\n')
    new_room_dim = (room_dim[0], room_dim[1])
    

    robots = {} 
    num_rob = int(lines[1]) # this gets the number of robots there. data type --> int
    start = 2 # 2 is the index of the position of the first robot 

    for i in range(0, num_rob): # adds the robot number and the starting coordinate for each robot in a dictionary 
        robots[i+1] = lines[start+i].split(" ")

    target_point = lines[start+num_rob].split(" ") # grabs the rendezvous point from the input.txt file. data type --> list 
    target_point[0] = int(target_point[0])
    target_point[1] = int(target_point[1])
    target_point.remove("\n")
    new_target_point = (target_point[0], target_point[1])

    rows = new_room_dim[0]  # the number of rows in the room 
    cols = new_room_dim[1]  # the number of columns in the room 
    temp = lines[start+num_rob+1:] # this is a list of lines that contains the room points information from input.txt 

    room = [] # this is where we will store the 2d list of the room 

    for row in range(0, rows): # this for loop iterates over the amount of rows there are and creates a new [] within the room variable 
        room.append([])
        for col in range(0, cols): # this for loop iterates over the amount of columns there are and appends a 1 or 0 for each coordinate in the room 
            room[row].append(0)
            room[row][col] = int(temp[row][col])

    f.close() # close the reading of input.txt

    return new_room_dim, robots, new_target_point, room


def validMoves(room, pos, room_dim):
    """
    takes in a room (2d list), a pos (tuple) and room_dim (tuple).
    Returns a list of tuples of the neighbouring spots. 
    """

    possible_moves = [] # where we will store tuples of possible moves that are valid

    max_row = room_dim[0] # the length of the room 
    max_col = room_dim[1] # the width of the room 

    pos_row = pos[0] # the pos row that we are moving from 
    pos_col = pos[1] # the pos col that we are moving from 
    # print('pos_row {} and pos_col {}'.format(pos_row, pos_col))


    if (pos_row - 1 >= 0) and (0 <= pos_col < max_col): # checking if moving up is a valid move 
        if room[pos_row-1][pos_col] == 0: possible_moves.append((pos_row-1, pos_col))

    if (pos_row + 1 < max_row) and (0 <= pos_col < max_col): # checking if moving down is a valid move 
        if room[pos_row+1][pos_col] == 0: possible_moves.append((pos_row+1, pos_col))
    
    if (pos_col - 1 >= 0) and (0 <= pos_row < max_row): # cheching if moving left is a valid move
        if room[pos_row][pos_col-1] == 0: possible_moves.append((pos_row, pos_col-1))

    if (pos_col + 1 < max_col) and (0 <= pos_row < max_row): # checking if moving right is a valid move 
        if room[pos_row][pos_col+1] == 0: possible_moves.append((pos_row, pos_col+1))

    return possible_moves


def targetReached(x1y1, x2y2):
    """
    Checks if two coordinates are the same.
    x1y1 is a ()
    x2y2 is a ()
    """ 

    return x1y1 == x2y2 


def strToInt(robots):
    """
    takes in robots which is a dictionary. Changes the str elements in the values to int. 
    """

    keys = robots.keys()

    for key in keys:
        value = robots[key]
        value[0] = int(value[0])
        value[1] = int(value[1])
        new_val = (value[0], value[1])
        robots[key] = new_val

    return robots
